import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

from datetime import datetime
from email import policy
from email.parser import BytesParser
from bz2 import BZ2Decompressor
import lzma
import gzip
import xml.etree.ElementTree as ET
import socket

default_path = "home/shared/DMARC/altair.ac6.fr/rua/"
save_path = "dmarc-visualizer-master/files/"
report_path = "dmarc-reports/"
year = datetime.now().year
month = datetime.now().month
decompressor = BZ2Decompressor()
report_data_template = {
    "xml_schema":'',
    "org_name":'./report_metadata/org_name',
    "org_email":'./report_metadata/email',
    "org_extra_contact_info":'',
    "report_id":'./report_metadata/report_id',
    "begin_date":'./report_metadata/date_range/begin',
    "end_date":'./report_metadata/date_range/end',
    "errors":'',
    "domain":'./policy_published/domain',
    "adkim":'./policy_published/adkim',
    "aspf":'./policy_published/aspf',
    "p":'./policy_published/p',
    "sp":'./policy_published/sp',
    "pct":'./policy_published/pct',
    "fo":'./policy_published/fo',
    "source_ip_address":'./record/row/source_ip',
    "source_country":'',
    "source_reverse_dns":'',
    "source_base_domain":'',
    "count":'./record/row/count',
    "spf_aligned":'./record/row/policy_evaluated/spf',
    "dkim_aligned":'./record/row/policy_evaluated/dkim',
    "dmarc_aligned":'./record/row/policy_evaluated/dmarc',
    "disposition":'./record/row/policy_evaluated/disposition',
    "policy_override_reasons":'',
    "policy_override_comments":'',
    "envelope_from":'',
    "header_from":'./record/identifiers/header_from',
    "envelope_to":'',
    "dkim_domains":'./record/auth_results/dkim/domain',
    "dkim_selectors":'./record/auth_results/dkim/selector',
    "dkim_results":'./record/auth_results/dkim/result',
    "spf_domains":'./record/auth_results/spf/domain',
    "spf_scopes":'',
    "spf_results":'./record/auth_results/spf/result',
}

if len(str(month)) == 1:
    month = "0" + str(month)

path = default_path + str(year) + "/" + str(month) + "/"

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

for report in reports:
    tree = ET.parse(report_path + report)
    root = tree.getroot()
    report_data = report_data_template.copy()
    date = root.find('./report_metadata/date_range/begin').text
    print(datetime.utcfromtimestamp(float(date)))
    print(socket.gethostbyaddr('37.59.46.135'))

    for key, value in report_data.items():
        try:
            test = root.find(value)
            print(key, test.text)
        except:
            print(key)
            continue