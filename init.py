import os
import sys
from datetime import datetime
from email import policy
from email.parser import BytesParser
from bz2 import BZ2Decompressor
import lzma
import gzip
import xml.etree.ElementTree as ET
import socket
from geolite2 import geolite2
import tldextract
import mysql.connector

os.chdir(os.path.dirname(sys.argv[0]))

with open('user.txt', 'r') as file:
    user, pwd = file.read().split('\n')

mydb = mysql.connector.connect(
  host="localhost",
  user=user,
  password=pwd
)

mycursor = mydb.cursor()

default_path = "home/shared/DMARC/altair.ac6.fr/rua/"
save_path = "dmarc-visualizer-master/files/"
report_path = "dmarc-reports/"
year = datetime.now().year
month = datetime.now().month
decompressor = BZ2Decompressor()
reader = geolite2.reader()

if len(str(month)) == 1:
    month = "0" + str(month)

path = default_path + str(year) + "/" + str(month) + "/"

report_data_template_meta = {
#    "xml_schema":'',
    "org_name":'./report_metadata/org_name',
    "org_email":'./report_metadata/email',
    "org_extra_contact_info":'./report_metadata/extra_contact_info',
    "report_id":'./report_metadata/report_id',
    "begin_date":'./report_metadata/date_range/begin',
    "end_date":'./report_metadata/date_range/end',
#    "errors":'',
    "domain":'./policy_published/domain',
    "adkim":'./policy_published/adkim',
    "aspf":'./policy_published/aspf',
    "p":'./policy_published/p',
    "sp":'./policy_published/sp',
    "pct":'./policy_published/pct',
    "fo":'./policy_published/fo'
}

report_data_template_record = {
    "source_ip_address":'row/source_ip',
    "source_country":'',
    "source_reverse_dns":'',
    "source_base_domain":'',
    "count":'row/count',
    "spf_aligned":'row/policy_evaluated/spf',
    "dkim_aligned":'row/policy_evaluated/dkim',
    "dmarc_aligned":'row/policy_evaluated/dmarc',
    "disposition":'row/policy_evaluated/disposition',
#    "policy_override_reasons":'',
#    "policy_override_comments":'',
    "envelope_from":'identifiers/envelope_from',
    "header_from":'identifiers/header_from',
    "envelope_to":'identifiers/envelope_to',
    "dkim_domain":'auth_results/dkim/domain',
    "dkim_selector":'auth_results/dkim/selector',
    "dkim_result":'auth_results/dkim/result',
    "spf_domain":'auth_results/spf/domain',
    "spf_scope":'auth_results/spf/scope',
    "spf_result":'auth_results/spf/result',
}

emails = os.listdir(path)

def unzip(email, path_in, path_out, overwrite = True):
    if email.endswith('.bz2'):
        new_mail = email.replace('.bz2', '')
        with open(path_in + email, 'rb') as file, open(path_out + new_mail, 'wb') as new_file:
            for data in iter(lambda : file.read(100 * 1024), b''):
                new_file.write(decompressor.decompress(data))

    if email.endswith('.gz'):
        new_mail = email.replace('.gz', '')
        with gzip.open(path_in + email) as f, open(path_out + new_mail, 'wb') as fout:
            file_content = f.read()
            fout.write(file_content)

    if email.endswith('.xz'):
        new_mail = email.replace('.xz', '')
        with lzma.open(path_in + email) as f, open(path_out + new_mail, 'wb') as fout:
            file_content = f.read()
            fout.write(file_content)
    
    if overwrite and not email.endswith('.mail'):
        os.remove(path_in + email)

for email in emails:
    unzip(email, path, path)

emails = os.listdir(path)

for email in emails:
    mail = BytesParser(policy=policy.default).parse(open(path + email, 'rb'))

    for attachment in mail.iter_attachments():
        name = attachment.get_filename()
        data = attachment.get_content()

        with open(save_path + name, 'wb') as f:
            f.write(data)

reports = os.listdir(save_path)

for report in reports:
    unzip(report, save_path, report_path, overwrite=False)

reports = os.listdir(report_path)
reports_data = []

for report in reports:
    tree = ET.parse(report_path + report)
    root = tree.getroot()
    report_data_meta = report_data_template_meta.copy()

    for key, value in report_data_template_meta.items():
        if key == 'begin_date' or key == 'end_date':
            date = root.find(value).text
            info = datetime.utcfromtimestamp(float(date))
            info = info.strftime('%Y-%m-%d %H:%M:%S')
            report_data_meta[key] = info
            continue

        try:
            info = root.find(value)
            report_data_meta[key] = info.text
        except AttributeError:
            if key == 'fo':
                report_data_meta[key] = '0'
                continue

            report_data_meta[key] = ''
            continue
    
    report_number = len(root.findall('record'))

    for report_n in range(report_number):
        report_data_record = report_data_template_record.copy()

        for key, value in report_data_template_record.items():
            value = './record[' + str(report_n+1) + ']/' + value

            try:
                info = root.find(value)
                report_data_record[key] = info.text
            except AttributeError:
                report_data_record[key] = ''
                continue
        
        ip_adress = root.find('./record/row/source_ip').text
        country = reader.get(ip_adress)['country']['iso_code']
        domain = socket.gethostbyaddr(ip_adress)[0]
        base_domain = tldextract.extract(domain).registered_domain
        report_data_record['source_country'] = country
        report_data_record['source_reverse_dns'] = domain
        report_data_record['source_base_domain'] = base_domain
    
        reports_data.append(report_data_meta | report_data_record)

with open('queries.sql', 'r') as file:
    sqlFile = file.read()

sqlCommands = sqlFile.split(';')

for command in sqlCommands:
    try:
        mycursor.execute(command)
    except mysql.connector.Error as error:
        print(error)