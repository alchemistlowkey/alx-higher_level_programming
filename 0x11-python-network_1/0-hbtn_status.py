#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""
from urllib.request import urlopen


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as response:
        body_bytes = response.read()
        body_string = body_bytes.decode("utf-8")


print("Body response:")
print("\t- type:", type(body_bytes))
print("\t- content:", body_bytes)
print("\t- utf8 content:", body_string)
