#!/usr/bin/python3
"""
A Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_r = r.json()
        if json_r:
            print("[{}] {}".format(json_r.get('id'), json_r.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
