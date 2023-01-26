#!/usr/bin/python3
'''UTF-8 Validation
'''


def validUTF8(data):
    """determine if a dataset represent valid UTF=8

    Args:
        data (List[int]): list of integers

    Returns:
        bool: True if utf-8 character
    """
    bytes_ = 0

    for i in data:
        if bytes_ == 0:
            if i >> 5 == 0b110 or i >> 5 == 0b1110:
                bytes_ = 1
            elif i >> 4 == 0b1110:
                bytes_ = 2
            elif i >> 3 == 0b11110:
                bytes_ = 3
            elif i >> 7 == 0b1:
                return False
        else:
            if i >> 6 != 0b10:
                return False
            bytes_ -= 1
    return bytes_ == 0
