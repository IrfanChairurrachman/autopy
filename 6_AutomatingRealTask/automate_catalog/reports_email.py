#!/usr/bin/env python3

import reports
import os
import emails
from datetime import date


def process_description(dir):
    
    paragraph = []

    for txt in os.listdir(dir):
        with open('{}/{}'.format(dir, txt)) as txt_file:
            lines = txt_file.readlines()
            # skip file if field are missing
            if len(lines) < 3:
                continue

            paragraph.append("name: {}<br/>weight: {}\n".format(lines[0].strip(), lines[1].strip()))

    return paragraph


if __name__ == "__main__":

    dir = 'supplier-data/descriptions'

    attachment = '/tmp/processed.pdf'
    title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    paragraph = "<br/><br/>".join(process_description(dir))

    reports.generate_report(attachment, title, paragraph)

    subject = "Upload Completed - Online Fruit Store"
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)