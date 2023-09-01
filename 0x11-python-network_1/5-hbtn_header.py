#!/usr/bin/python3

"""
This Python script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.

The value of this variable is different for each request.

Usage: ./5-hbtn_header.py <url>
"""


import requests
import sys


def hbtn_header(url):
    response = requests.get(url)
    request_id = response.headers['X-Request-Id']
    print(request_id)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        url = sys.argv[1]
        hbtn_header(url)
    else:
        print('Usage: ./5-hbtn_header.py <url>')
