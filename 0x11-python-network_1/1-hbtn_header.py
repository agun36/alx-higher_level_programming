#!/usr/bin/python3

"""
This Python script takes in a URL, sends a request to the URL and displays
the value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <url>
"""


import urllib.request
import sys


def hbtn_header(url):
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        request_id = headers['X-Request-Id']
        print(request_id)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        hbtn_header(url)
    else:
        print('Usage: ./1-hbtn_header.py <url>')
