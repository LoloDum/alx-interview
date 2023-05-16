#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    number_bytes = 0

    num_1 = 1 << 7
    num_2 = 1 << 6

    for i in data:

        num_byte = 1 << 7

        if number_bytes == 0:

            while num_byte & i:
                number_bytes += 1
                num_byte = num_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & num_1 and not (i & num_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
