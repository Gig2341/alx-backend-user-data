#!/usr/bin/env python3
'''a module that returns the log message obfuscated'''


import re
from typing import List


def filter_datum(fields: [List], redaction: str, message: str, \
        separator: str) -> str:
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}', \
                f'{f}={redaction}{separator}', message)
    return message
