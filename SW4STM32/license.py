import mysql.connector
import uuid
import sys
import datetime
import tkinter.messagebox


with open('root.txt', 'r') as file:
    user, pwd = file.read().split('\n')

with open('license.lic', 'r') as file:
    licenses = file.read().split('\n')

get_key = """
    SELECT key_
    FROM license.licenses
    WHERE mac = %s AND email = %s
    """

get_date = """
    SELECT until
    FROM license.licenses
    WHERE mac = %s AND email = %s
    """


try:
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
except:
    sys.exit('no_mac')

mydb = mysql.connector.connect(host="localhost", user=user, password=pwd, database='LICENSE')
mycursor = mydb.cursor(buffered=True)

email = str(input('Please enter your registered email address\n'))

product = licenses[0]
licenses.pop(0)

for license in licenses:
    data = license.split('#')
    feature = data[0].replace('fr.ac6.feature.', '')
    type = data[1].replace('type=', '')
    until = data[2].replace('until=', '')
    key = data[3].replace('key=', '')

    mycursor.execute(get_key, [mac, email])
    try:
        db_key = mycursor.fetchone()[0]
    except:
        sys.exit('unknown_email')
    
    mycursor.execute(get_date, [mac, email])
    try:
        date = mycursor.fetchone()[0]
    except:
        sys.exit('no_date')

    if key != db_key:
        sys.exit('wrong_key')
    
    current = datetime.datetime.date(datetime.datetime.now())

    if current <= date:
        sys.exit('valid_license')
    else:
        choice = tkinter.messagebox.askquestion('Expired License','Would you like to renew your license ?')
        if choice == 'yes':
            next_month = current.replace(day = 28) + datetime.timedelta(days = 4)
            last_day = next_month - datetime.timedelta(days = next_month.day)
            print(last_day)