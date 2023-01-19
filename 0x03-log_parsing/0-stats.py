#!/usr/bin/python3
'''Parse HTTP request logs
'''
import sys


# def verify_input():
#     '''determines if the format is as described or to skip the line
#     '''
#     log_format = ''
#     pass

def parse(inpt, size):
    '''Prints logs'''
    print("File size: {:d}".format(size))
    for i in sorted(inpt.keys()):
        if inpt[i] != 0:
            print("{}: {:d}".format(i, inpt[i]))


status = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
       "404": 0, "405": 0, "500": 0}
counter = 0
size = 0

try:
    for line in sys.stdin:
        if counter != 0 and counter % 10 == 0:
            parse(status, size)

        statusList = line.split()
        counter += 1

        try:
            size += int(statusList[-1])
        except:
            pass

        try:
            if statusList[-2] in status:
                status[statusList[-2]] += 1
        except:
            pass
    parse(status, size)


except KeyboardInterrupt:
    parse(status, size)
    raise
