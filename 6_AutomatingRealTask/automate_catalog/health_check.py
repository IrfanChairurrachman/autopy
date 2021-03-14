#!/usr/bin/env python3

import shutil
import psutil
import emails
import socket
import os
import time

"""
    source and thanks to:
    https://github.com/kumbasar/IT-Automation-with-Python/blob/main/Automate-updating-catalog-information/health_check.py
    I use this for health_check because the code really readable and effective
"""

def alert(subject):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."

    message = emails.generate_email(sender, receiver, subject, body)
    emails.send_email(message)


def checkCPU(threshold=80):
    if psutil.cpu_percent() > threshold:
        alert("Error - CPU usage is over 80%")


def checkMEM(threshold=500):
    if psutil.virtual_memory().available/(1024*1024) < threshold:
        alert("Error - Available memory is less than 500MB")


def checkHDD(threshold=20):
    if psutil.disk_usage('/').percent < threshold:
        alert("Error - Available disk space is less than 20%")


def checkLocalhost(localhost='127.0.0.1'):
    if socket.gethostbyname('localhost') != localhost:
        alert("Error - localhost cannot be resolved to 127.0.0.1")


if __name__ == "__main__":

    sleep_time = 60

    while True:
        checkLocalhost()
        checkHDD()
        checkMEM()
        checkCPU()
        time.sleep(sleep_time)