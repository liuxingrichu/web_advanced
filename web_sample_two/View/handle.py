#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_PATH)


def handle_index():
    import time
    with open(os.path.join(BASE_PATH, 'Template/index.html'), 'rb') as f:
        data = f.read()
    data = data.replace(b"@uuuu", str(time.time()).encode("utf-8"))
    return [data, ]


def handle_date():
    return ["<h1>Hello, date!</h1>".encode("utf-8"), ]
