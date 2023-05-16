import argparse
import mysql.connector

parser = argparse.ArgumentParser(description="License Checker",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-i", "--init", action="store_true", help="create brand new MySQL database")
parser.add_argument("-m", "--mac", action='store', help="MAC address to lookup")

args = parser.parse_args()
config = vars(args)

with open('root.txt', 'r') as file:
    user, pwd = file.read().split('\n')

create_db = """
    CREATE TABLE LICENSES (
    record_id INTEGER,
    mac_address VARCHAR(255),
    client_name VARCHAR(255),
    client_email VARCHAR(255),
    license_type VARCHAR(255),
    license_features VARCHAR(255),
    expires VARCHAR(255),
    currently_effective BOOLEAN,
    PRIMARY KEY (record_id))
    """

get_status = """
    SELECT currently_effective
    FROM license.licenses
    WHERE mac_address = %s
    """

def create_database():
    mydb = mysql.connector.connect(host="localhost", user=user, password=pwd)
    mycursor = mydb.cursor(buffered=True)
    mycursor.execute('CREATE DATABASE LICENSE')
    mydb.close()

    mydb = mysql.connector.connect(host="localhost", user=user, password=pwd, database='LICENSE')
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute(create_db)
    mydb.commit()


def check_license(mac_address):
    mydb = mysql.connector.connect(host="localhost", user=user, password=pwd, database='LICENSE')
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute(get_status, list([mac_address]))
    status = 0
    try:
        status = mycursor.fetchone()[0]
    except TypeError:
        print('Unknown MAC Address')

    if status == 1:
        print('Valid License')
    else:
        print('Invalid License')


if config['init']:
    create_database()
else:
    check_license(config['mac'])