#!/usr/bin/python3
"""
A Python script that takes 2 arguments in order to solve this challenge
"""

import requests
from sys import argv


if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
    r = requests.get(url)
    commits = r.json()
    for message in commits[:10]:
        sha = message["sha"]
        author = message['commit']['author']['name']
        print("{}: {}".format(sha, author))
