#!/usr/bin/env python3
# Import module
import csv
import sys
import re
import operator

error = {}
per_user = {}

with open('syslog.log') as file:
    for log in file:
        result = re.search(r"ticky: ([INFO|ERROR]*): (['\w ]*) [\[[#\d]*\]?]? ?\(([.\w]*)\)$", log)

        if result[3] not in per_user:
            per_user[result[3]] = [0, 0]

        if result[1] == 'INFO':
            per_user[result[3]][0] += 1
        elif result[1] == 'ERROR':
            per_user[result[3]][1] += 1
            if result[2] not in error:
                error[result[2]] = 0
            error[result[2]] += 1
        
        print("{} {} {}".format(result[1], result[2], result[3]))

print(sorted(per_user.items()))
print(sorted(error.items(), key = operator.itemgetter(1), reverse=True))