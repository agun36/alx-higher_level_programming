#!/usr/bin/python3

"""
This Python script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.

The value of this variable is different for each request.

Usage: ./5-hbtn_header.py <url>
"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    
    if 'X-Request-Id' in response.headers:
        print(response.headers['X-Request-Id'])
    else:
        print("Header 'X-Request-Id' not found in the response.")
