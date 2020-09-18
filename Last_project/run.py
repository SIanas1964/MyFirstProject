#! /usr/bin/env python3
"""
Sends the fruit data to the django server to add it
"""

import os
import requests

path = "supplier-data/descriptions"
url = "http://35.192.134.68/fruits/"
descriptions_list = os.listdir(path)

for description_file in descriptions_list :
    with open(path + "/" + description_file, 'r') as description :
        lines = description.readlines()
        description_data = {"name": lines[0].strip('\n'), "weight":int(lines[1].strip("lbs") , "description": lines[2], "image_name": description_file.strip(".txt") + ".jpeg"}
    r = requests.post(url, json = description_data)
    print("Request status code is {}".format(r.status_code))