#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys


line_count = 0
total_file_size = 0

status_code = {
    "200": 0, "301": 0,
    "400": 0, "401": 0,
    "403": 0, "404": 0,
    "405": 0, "500": 0
    }

try:
    for line in sys.stdin:
        args = line.split(' ')

        if len(args) > 2:
            status_line = args[-2]
            file_size = args[-1]

            if status_line in status_code:
                status_code[status_line] += 1
            total_file_size += int(file_size)
            line_count += 1

            if line_count == 10:
                print('File size: {:d}'.format(total_file_size))
                sorted_keys = sorted(status_code.keys())

                for key in sorted_keys:
                    value = status_code[key]

                    if value != 0:
                        print('{}: {}'.format(key, value))
                    line_count = 0

finally:
    print("File size: {:d}".format(total_file_size))
    sorted_keys = sorted(status_code.keys())

    for key in sorted_keys:
        value = status_code[key]
        if value != 0:
            print("{}: {}".format(key, value))
