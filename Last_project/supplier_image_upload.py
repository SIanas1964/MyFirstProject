#!/usr/bin/env python3
"""
upload images to webserver
"""
import os
import requests

path = ""
images_list = [ image for image in os.listdir(path) if ".jpeg" in image ]
url = ""

for image in images_list:
    image_file = open(path + "/" + image, 'rb')
    r = requests.post(url, file={"file": image_file})
    print("Request returned code: {}".format(r.status_code))
