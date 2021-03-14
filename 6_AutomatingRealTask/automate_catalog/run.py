#!/usr/bin/env python3

import os
import re
import requests


def generate_description(dir, url):
    
    descriptions = []

    for txt in os.listdir(dir):
        with open('{}/{}'.format(dir, txt)) as txt_file:
            lines = txt_file.readlines()
            
            if len(lines) < 3:
                continue

            weight = int(re.search(r"^(\d+)", lines[1].strip()).group())

            descriptions.append({
                "name": lines[0].strip(),
                "weight": weight,
                "description": "".join(lines[2:]).strip(),
                "image_name": txt.replace(".txt", ".jpeg")
            })

    for description in descriptions:
        response = requests.post(url, json=description)
        if not response.ok:
            raise Exception("FAILED to POST, reponse: {}, text title: {}".format(response.status_code, description['name']))
        print("Feedback title: {} added!, response: {}".format(description['title'], response.status_code))

if __name__ == "__main__":
    descriptions = getDescriptions('supplier-data/descriptions')
    dir = 'supplier-data/descriptions'
    url = 'http://localhost/fruits/'
    generate_description(dir, url)