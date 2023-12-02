#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    x_request_id = r.headers.get('X-Request-Id')
    print(x_request_id)
