import mysql.connector
import uuid
import tkinter
import tkinter.messagebox
import webbrowser
import psutil


with open('root.txt', 'r') as file:
    user, pwd = file.read().split('\n')

get_status = """
    SELECT currently_effective
    FROM license.licenses
    WHERE mac_address = %s
    """

try:
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
except:
    mac = ''


def kill_eclipse():
    for proc in psutil.process_iter():
                if proc.name() == 'eclipse.exe':
                    proc.kill()
                    print('Closing System Workbench...')


mydb = mysql.connector.connect(host="localhost", user=user, password=pwd, database='LICENSE')
mycursor = mydb.cursor(buffered=True)

mycursor.execute(get_status, list([mac]))
status = -1
try:
    status = mycursor.fetchone()[0]
except TypeError:
    choice = tkinter.messagebox.askquestion('Unknown MAC Address','This MAC address is not registered with a license.\nWould you like to create an account ?')
    if choice == 'yes':
        webbrowser.open('https://www.openstm32.org/tiki-register.php')
        kill_eclipse()
    else:
        kill_eclipse()

if status == 1:
    pass
elif status == 0:
    choice = tkinter.messagebox.askquestion('Invalid License','The license associated with this MAC address is expired.\nWould you like to renew your license ?')
    if choice == 'yes':
        webbrowser.open('https://www.openstm32.org/tiki-login_scr.php')
        kill_eclipse()
    else:
        kill_eclipse()
else:
    tkinter.messagebox.showinfo('Error','The MAC address of this computer could not be found.')