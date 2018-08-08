import csv
import sqlite3
import xml.etree.ElementTree as ET

from config import STORAGE, FILE


def get_test_data():
    """
    Return list of values from the file specified in config.py
    """
    if STORAGE == "csv":
        with open(FILE) as f:
            test_data = list(csv.reader(f))[1:]

    elif STORAGE == "xml":
        with open(FILE) as f:
            tree = ET.parse(f)
            container = tree.findall("account")
            test_data = [[i.find('from_username').text,
                          i.find('from_password').text,
                          i.find('to_username').text,
                          i.find('to_password').text] for i in container]

    elif STORAGE == "sqlite":
        con = sqlite3.connect(FILE)
        cur = con.cursor()
        cur.execute("""SELECT from_username, from_password,        
                    to_username, to_password FROM accounts""")
        test_data = cur.fetchall()
        cur.close()
        con.close()

    else:
        raise ValueError('Invalid data type. Specify correct STORAGE in settings.py')
    return test_data
