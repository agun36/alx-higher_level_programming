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
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    status = r.status_code
    print(r.text) if status < 400 else print(
        "Error code: {}".format(r.status_code))
