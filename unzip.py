import os
from bz2 import BZ2Decompressor
import lzma
import gzip

decompressor = BZ2Decompressor()

def unzip(email, path):
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