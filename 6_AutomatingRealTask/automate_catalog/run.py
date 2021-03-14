#!/usr/bin/env python3

import os
import re
import requests


def generate_description(dir, url):
    
    fruits = []

    for txt in os.listdir(dir):
        with open('{}/{}'.format(dir, txt)) as txt_file:
            lines = txt_file.readlines()
            
            if len(lines) < 3:
                continue

            weight = int(re.search(r"^(\d+)", lines[1].strip()).group())

            fruits.append({
                "name": lines[0].strip(),
                "weight": weight,
                "description": "".join(lines[2:]).strip(),
                "image_name": txt.replace(".txt", ".jpeg")
            })

    for fruit in fruits:
        response = requests.post(url, json=fruit)
        if not response.ok:
            raise Exception("FAILED to POST, reponse: {}, fruit: {}".format(response.status_code, fruit['name']))
        print("Fruit: {} added!, response: {}".format(fruit['name'], response.status_code))

if __name__ == "__main__":
    dir = 'supplier-data/descriptions'
    url = 'http://localhost/fruits/'
    generate_description(dir, url)