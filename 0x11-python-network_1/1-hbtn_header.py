#!/usr/bin/python3
"""A script
- sends a request to the URL and displays the value
"""
from sys import argv
import urllib.request

if __name__ == "__main__":
    url = argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
