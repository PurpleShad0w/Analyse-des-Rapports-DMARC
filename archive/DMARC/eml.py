from functools import reduce
from operator import getitem
import re
import geolite2
import eml_parser

reader = geolite2.reader()
ep = eml_parser.EmlParser()

def get_item_from_dict(dataDict, mapList):
    return reduce(getitem, mapList, dataDict)

report_data_template_ruf = {
    'subject':'header:subject',
    'from':'header:from',
    'to':'header:to',
    'date':'header:date',
    'source_ip':'attachment:0:content_header:x-onpremexternalip',
    'country':'',
    'auth_results':'attachment:0:content_header:authentication-results',
    'spf':'',
    'dkim':'',
    'tls':'',
    'dmarc':'',
    'message_id':'header:header:message-id',
    'full_mail':''
}


def analyze_eml(path_report, report):
    with open(path_report + report, 'rb') as f:
        feedback_report = f.read()

    parsed_report = report_data_template_ruf.copy()
    parsed_eml = ep.decode_email_bytes(feedback_report)

    for key, value in report_data_template_ruf.items():
        value = value.split(':')

        for i in range(len(value)):
            if len(value[i]) == 1:
                value[i] = int(value[i])

        try:
            info = get_item_from_dict(parsed_eml, value)
            parsed_report[key] = str(info)
        except:
            if key == 'full_mail':
                parsed_report[key] = str(parsed_eml)
                continue

            parsed_report[key] = ''

    ip_address = parsed_report['source_ip'].replace('[\'', '').replace('\']', '')
    if ip_address != '':
        try:
            country = reader.get(ip_address)['country']['iso_code']
        except TypeError:
            country = ''
        parsed_report['country'] = country

    results = parsed_report['auth_results']
    spf = re.search('spf=(.*) smtp.mailfrom', results).group(1)
    dkim = re.search('dkim=(.*) header.d', results).group(1)
    tls = re.search('tls=(.*) key.ciphersuite', results).group(1)
    dmarc = re.search('dmarc=(.*) header', results).group(1)
    parsed_report['spf'] = spf
    parsed_report['dkim'] = dkim
    parsed_report['tls'] = tls
    parsed_report['dmarc'] = dmarc

    return parsed_report