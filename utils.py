import csv
import random
import sqlite3
import string
import xml.etree.ElementTree as ET
import requests
from config import STORAGE, FILE
import logging
import os
import json


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


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_screenshot(driver):
    file_path = os.path.join(os.getcwd(), "logs", "screenshots",
                             "{}.png".format(random_string_generator(size=5)))
    driver.save_screenshot(file_path)
    file_link = img_uploader(file_path)
    logging.error(
        "Element can't be located. Check screenshot for details: {}".format(file_link))

    
def img_uploader(img_path):
    url = os.environ.get("upload_api")
    file = {"file": open(img_path, "rb")}
    my_session = requests.Session()
    res = my_session.post(url, files=file)
  
    return res.text
