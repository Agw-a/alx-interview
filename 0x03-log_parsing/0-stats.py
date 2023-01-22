#!/usr/bin/python3
'''Parse HTTP request logs/print from stdin
'''
from sys import stdin

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

n = 0


def print_status():
    '''Print logs
    '''
    print("File size: {}".format(n))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code]:
            print("{}: {}".format(n, status_codes[n]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                item = line.split()
                n += int(item[-1])
                if item[-2] in status_codes:
                    status_codes[item[-2]] += 1
            except:
                pass
            if count == 9:
                print_status()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_status()
        raise
    print_status()
