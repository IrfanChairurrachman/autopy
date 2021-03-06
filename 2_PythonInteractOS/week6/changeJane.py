#!/usr/bin/env python3
import sys
import subprocess

with open(sys.argv[1], mode='r') as file:
  for line in file.readlines():
    name = line.strip()
    new_name = name.replace('jane', 'jdoe')
    subprocess.run(['mv', name, new_name])
