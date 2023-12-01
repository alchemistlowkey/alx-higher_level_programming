#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value
"""

from urllib.request import urlopen
from sys import argv


if __name__ == '__main__':
    url = argv[1]
    with urlopen(url) as response:
        data = response.info()
        print(data['X-Request-Id'])
