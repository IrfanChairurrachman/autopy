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
        
        print("{} {} {}".format(result[1], result[2], result[3]))

print(sorted(per_user.items()))
print(sorted(error.items(), key = operator.itemgetter(1), reverse=True))