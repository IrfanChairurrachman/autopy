#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
path = 'supplier-data/images/'

list_img = [os.path.join(path, img) for img in os.listdir(path) if '.jpeg' in img]

for img in list_img:
    with open(img, 'rb') as opened:
        r = requests.post(url, files={'file': opened})