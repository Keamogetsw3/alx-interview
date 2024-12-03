#!/usr/bin/python3
import sys
""" module to reads stdin line by line and computes metrics """


def _print(status_dct, total_size):
    """
    Displays the summary of file statistics, including the total file size
    and counts of different status codes.

    Args:
        status_dct: A dictionary with status codes as keys (strings)
        total_size: The total size of the files processed, in bytes.

    Returns:
        None: don’t print anything for this status code
    """
    print("Total file size: {}".format(total_size))
    for code, count in sorted(status_dct.items()):
        if count != 0:
            print("{}: {}".format(code, count))

total_size = 0
status_code = 0
line_count = 0
status_dct = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parts = line.split()
        parts = parts[::-1]

        if len(parts) > 2:
            line_count += 1

            if line_count <= 10:
                total_size += int(parts[0])
                status_code = parts[1]

                if status_code in status_dct:
                    status_dct[status_code] += 1

            if line_count == 10:
                _print(status_dct, total_size)
                line_count = 0

finally:
    _print(status_dct, total_size)
