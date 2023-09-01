#!/usr/bin/python3

"""
This Python script takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).

If the request fails, it prints the error code.

Usage: ./3-error_code.py <url>
"""


import urllib.request
import sys


def get_body(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            return body
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
        return None


if __name__ == "__main__":
    url = sys.argv[1]
    body = get_body(url)
    if body:
        print(body)
