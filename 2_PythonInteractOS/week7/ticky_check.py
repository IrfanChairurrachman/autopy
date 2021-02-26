#!/usr/bin/env python3
# Import module
import csv
import sys
import re
import operator

# Create dictionary
error = {}
per_user = {}

# Open file and close after do things
with open('syslog.log') as file:
    # Iterate each line in file
    for log in file.readlines():
        # search format with regex
        result = re.search(r"ticky: ([INFO|ERROR]*): (['\w ]*) [\[[#\d]*\]?]? ?\(([.\w]*)\)$", log)

        # initiate user in dict if doesn't exist before
        if result[3] not in per_user:
            # first list for INFO, second for ERROR
            per_user[result[3]] = [0, 0]

        # add INFO and ERROR
        if result[1] == 'INFO':
            per_user[result[3]][0] += 1
        elif result[1] == 'ERROR':
            per_user[result[3]][1] += 1
            # Add error to error dict
            if result[2] not in error:
                error[result[2]] = 0
            error[result[2]] += 1

# Sorted dictionary
per_user = sorted(per_user.items())
error = sorted(error.items(), key = operator.itemgetter(1), reverse=True)
print(per_user)
print(error)

# Write into csv
with open('error_message.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Error', 'Count'])
    for err in error:
        writer.writerow(err)

with open('user_statistics.csv', mode='w') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Username', 'INFO', 'ERROR'])
    for usr in per_user:
        writer.writerow([usr[0], usr[1][0], usr[1][1]])