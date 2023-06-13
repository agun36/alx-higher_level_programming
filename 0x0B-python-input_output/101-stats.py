#!/usr/bin/python3
'Log Parsing'
import sys

items_list = [200, 301, 400, 401, 403, 404, 405, 500]
try:
    total = 0
    final = []
    for index, line in enumerate(sys.stdin, 1):
        if line:
            line_split = line.split()
            if len(line_split) > 2:
                if line_split[-1].isnumeric() and line_split[-2].isnumeric():
                    size = line_split[-1]
                    status = line_split[-2]
                    total += int(size)
            if len(status) > 0 and int(status) in status_list:
                final.append(int(status))
        if index % 10 == 0:
            print('File size: {}'.format(total))
            for i in items_list:
                if i in final:
                    status_count = final.count(i)
                    print("{}: {}".format(i, status_count))
except Exception:
    pass

finally:
    print('File size: {}'.format(total))
    for i in items_list:
        if i in final:
            status_count = final.count(i)
            print("{}: {}".format(i, status_count))
