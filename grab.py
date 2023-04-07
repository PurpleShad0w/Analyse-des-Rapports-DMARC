import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

from datetime import datetime
from email import policy
from email.parser import BytesParser
import gzip
import shutil

default_path = "home/shared/DMARC/altair.ac6.fr/rua/"
save_path = "dmarc-visualizer-master/files/"
year = datetime.now().year
month = datetime.now().month

if len(str(month)) == 1:
    month = "0" + str(month)

path = default_path + str(year) + "/" + str(month) + "/"
emails = os.listdir(path)

for email in emails:
    mail = BytesParser(policy=policy.default).parse(open(path + email, 'rb'))
    print("Fetching " + email + " !")

    for attachment in mail.iter_attachments():
        name = attachment.get_filename()
        data = attachment.get_content()

        with open(save_path + name, 'wb') as f:
            f.write(data)

zip_files = os.listdir(save_path)

for zip_file in zip_files:
    print(" ")