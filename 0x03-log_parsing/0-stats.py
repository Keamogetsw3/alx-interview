#!/usr/bin/python3

import sys

def display_statistics(status_codes_count, total_size):
    """
    Displays the summary of file statistics, including the total file size
    and counts of different status codes.

    Args:
        status_codes_count (dict): A dictionary with status codes as keys (strings)
                                    and their respective counts as values (integers).
        total_size (int): The total size of the files processed, in bytes.

    Returns:
        None: This function prints the results to the standard output.
    """
    print("Total file size: {}".format(total_size))
    for code, count in sorted(status_codes_count.items()):
        if count != 0:
            print("{}: {}".format(code, count))

total_size = 0
status_code = 0
line_count = 0
status_codes_count = {
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

                if status_code in status_codes_count:
                    status_codes_count[status_code] += 1

            if line_count == 10:
                display_statistics(status_codes_count, total_size)
                line_count = 0

finally:
    display_statistics(status_codes_count, total_size)
