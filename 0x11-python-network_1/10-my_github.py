#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = argv[1]
    passtoken = argv[2]
    giturl = "https://api.github.com/user"
    r = requests.get(giturl, auth=HTTPBasicAuth(username, passtoken))
    if r.status_code == 200:
        print(r.json()['id'])
    else:
        print(None)
