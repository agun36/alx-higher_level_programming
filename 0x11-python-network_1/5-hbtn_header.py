#!/usr/bin/python3

"""
This Python script takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header.

The value of this variable is different for each request.

Usage: ./5-hbtn_header.py <url>
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
        print("Header 'X-Request-Id' not found in the response.")
