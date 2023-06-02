import mysql.connector
import uuid
import tkinter
import tkinter.messagebox
import webbrowser
import os
import sys


with open('root.txt', 'r') as file:
    user, pwd = file.read().split('\n')

get_status = """
    SELECT currently_effective
    FROM license.licenses
    WHERE mac_address = %s
    """

url_register = 'https://www.openstm32.org/tiki-register.php'
url_login = 'https://www.openstm32.org/tiki-login_scr.php'

try:
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
except:
    mac = ''

mydb = mysql.connector.connect(host="localhost", user=user, password=pwd, database='LICENSE')
mycursor = mydb.cursor(buffered=True)

mycursor.execute(get_status, list([mac]))
status = -1
try:
    status = mycursor.fetchone()[0]
except TypeError:
    choice = tkinter.messagebox.askquestion('Unknown MAC Address','This MAC address is not registered with a license.\nWould you like to create an account ?')
    if choice == 'yes':
        webbrowser.open(url_register)
        # this prevents the program from stopping somehow
    sys.exit('Software Did Not Launch')

if status == 1:
    # need command to launch SW4STM32 on any platform (linux mainly)
    os.startfile('SW4STM32\eclipse.exe.lnk')
    sys.exit('Software Launched')
elif status == 0:
    choice = tkinter.messagebox.askquestion('Invalid License','The license associated with this MAC address is expired.\nWould you like to renew your license ?')
    if choice == 'yes':
        webbrowser.open(url_login)
    sys.exit('Software Did Not Launch')
else:
    tkinter.messagebox.showinfo('Error','Unexpected result.')