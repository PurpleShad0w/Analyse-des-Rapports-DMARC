import datetime
import mysql.connector
import sys
import tkinter.messagebox
import tkinter.simpledialog
import uuid


with open('root.txt', 'r') as file:
    user, pwd, host = file.read().split('\n')

with open('license.lic', 'r') as file:
    licenses = file.read().split('\n')

get_key = """
    SELECT key_
    FROM LICENSE.LICENSES
    WHERE mac = %s AND email = %s
    """

get_date = """
    SELECT until
    FROM LICENSE.LICENSES
    WHERE mac = %s AND email = %s
    """

get_mac = """
    SELECT mac
    FROM LICENSE.LICENSES
    WHERE key_ = %s AND email = %s
    """

update_mac = [
    "SET SQL_SAFE_UPDATES = 0;",
    "UPDATE LICENSE.LICENSES SET mac = REPLACE(mac, %s, %s);",
    "SET SQL_SAFE_UPDATES = 1;"
    ]

check_email = """
    SELECT *
    FROM LICENSE.LICENSES
    WHERE email = %s
    """


try:
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
except:
    sys.exit('no_mac')

mydb = mysql.connector.connect(host=host, user=user, password=pwd, database='LICENSE')
mycursor = mydb.cursor(buffered=True)

root = tkinter.Tk()
root.wm_state('iconic')
email = tkinter.simpledialog.askstring("Login", "Please enter your registered email address.")

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
        mycursor.execute(get_mac, [key, email])
        try:
            db_mac = mycursor.fetchone()[0]
            choice = tkinter.messagebox.askyesno('Mismatched MAC address',"Would you like to switch the registered MAC address to this computer's ?")
            if choice:
                mycursor.execute(update_mac[0])
                mycursor.execute(update_mac[1], [db_mac, mac])
                mycursor.execute(update_mac[2])
                mydb.commit()
                sys.exit('update_acceptance') # LAUNCH
            else:
                sys.exit('update_refusal') # LAUNCH
        except:
            mycursor.execute(check_email, [email])
            try:
                mycursor.fetchone()[0]
                tkinter.messagebox.showwarning('Incorrect Key','This license key is not associated with your account.')
                sys.exit('incorrect_key') # DO NOT LAUNCH
            except:
                tkinter.messagebox.showwarning('Unknown Email','This email address is not associated with any account.')
                sys.exit('unknown_email') # DO NOT LAUNCH
    
    mycursor.execute(get_date, [mac, email])
    try:
        date = mycursor.fetchone()[0]
    except:
        tkinter.messagebox.showwarning('No Date','Could not find a validation date for your license, please visit ac6.fr to reach support.')
        sys.exit('no_date') # DO NOT LAUNCH

    if key != db_key:
        tkinter.messagebox.showwarning('Wrong Key','This license key is not associated with your account.')
        sys.exit('wrong_key') # DO NOT LAUNCH
    
    current = datetime.datetime.date(datetime.datetime.now())

    if current <= date:
        sys.exit('valid_license') # LAUNCH
    else:
        tkinter.messagebox.showwarning('Expired License','Please visit ac6.fr in order to renew your System Workbench license.')
        sys.exit('expired_license') # DO NOT LAUNCH