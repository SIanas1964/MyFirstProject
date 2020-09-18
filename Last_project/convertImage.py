#!/usr/bin/env python3
"""
Converts images in path to the same file to jpeg format in (600,400) size 
"""
import os
from PIL import Image

path = "supplier-data/images"
images_dir = os.listdir(path)

for image_file in images_dir:
    im = Image.open(path + "/" + image_file)
    im.convert("RGB").resize((600,400)).save(path + "/" + image_file + ".jepg", "JPEG")
