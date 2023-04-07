import os
import sys

os.chdir(os.path.dirname(sys.argv[0]))

from datetime import datetime
from email import policy
from email.parser import BytesParser
from bz2 import BZ2Decompressor
import lzma
import gzip

default_path = "home/shared/DMARC/altair.ac6.fr/rua/"
save_path = "dmarc-visualizer-master/files/"
year = datetime.now().year
month = datetime.now().month
decompressor = BZ2Decompressor()

if len(str(month)) == 1:
    month = "0" + str(month)

path = default_path + str(year) + "/" + str(month) + "/"
emails = os.listdir(path)

for email in emails:
    if email.endswith('.bz2'):
        new_mail = email.replace('.bz2', '')
        with open(path + email, 'rb') as file, open(path + new_mail, 'wb') as new_file:
            for data in iter(lambda : file.read(100 * 1024), b''):
                new_file.write(decompressor.decompress(data))
        os.remove(path + email)

    if email.endswith('.gz'):
        new_mail = email.replace('.gz', '')
        with gzip.open(path + email) as f, open(path + new_mail, 'wb') as fout:
            file_content = f.read()
            fout.write(file_content)
        os.remove(path + email)

    if email.endswith('.xz'):
        new_mail = email.replace('.xz', '')
        with lzma.open(path + email) as f, open(path + new_mail, 'wb') as fout:
            file_content = f.read()
            fout.write(file_content)
        os.remove(path + email)

emails = os.listdir(path)

for email in emails:
    mail = BytesParser(policy=policy.default).parse(open(path + email, 'rb'))

    for attachment in mail.iter_attachments():
        name = attachment.get_filename()
        data = attachment.get_content()

        with open(save_path + name, 'wb') as f:
            f.write(data)