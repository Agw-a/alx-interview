#!/usr/bin/python3
'''Parse HTTP request logs
'''
import sys
import re
import random

# def verify_input():
#     '''determines if the format is as described or to skip the line
#     '''
#     log_format = ''
#     pass
counter = 0
n = 0


def printLogs(size, status, response):
    '''Print HTTP logs
    '''
    print("File size: {:d}".format(size))
    for i in status:
        if response[i] > 0:
            print('{}: {}'.format(i, response[i]))
    
def parse():
    '''Prse http logs
    '''
    try:
        i = 0
        fSize = 0
        statusResponse = {
            '200':0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
        }
        statusCode = ['200', '301', '400', '401', '403', '404', '405', '500']
        for lines in sys.stdin:
            queryStr = re.search(r'[2-5]0[0-5] \d+', lines)
            if queryStr is None:
                continue
            queryStr = queryStr.group()
            values = queryStr.split(' ')
            status = values[0]
            size = values[1]
            if status in statusCode:
                statusResponse[status] += 1
            try:
                fSize += int(size)
            except Exception:
                pass
            if n == 9:
                n = 0
                printLogs(fSize, statusCode, statusResponse)
                continue
            n += 1
    except KeyboardInterrupt as e:
        printLogs(fSize, statusCode, statusResponse)
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    parse()