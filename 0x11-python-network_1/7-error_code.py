#!/usr/bin/python3

"""
This Python script takes in a URL, sends a request to the URL
and displaysthe body of the response.

If the HTTP status code is greater than or equal to 400,
print: Error code:
followed by the value of the HTTP status code.

You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)
Please test your script in the sandbox provided, using the web server
running on port 5000

Usage: ./7-error_code.py <url>
"""


import requests
import sys


def get_body(url):
    response = requests.get(url)
    if response.status_code >= 400:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.content)


if __name__ == "__main__":
    url = sys.argv[1]
    get_body(url)
