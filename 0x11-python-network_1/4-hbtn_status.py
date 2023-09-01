#!/usr/bin/python3

"""
This Python script fetches https://alx-intranet.hbtn.io/status
using the requests package.

The body of the response must be displayed like the following example
(tabulation before -).

Usage: ./4-hbtn_status.py
"""


import requests


def hbtn_status():
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print('Body response:')
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == '__main__':
    hbtn_status()
