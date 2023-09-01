#!/usr/bin/python3

"""
This Python script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8).

Usage: ./2-post_email.py <url> <email>
"""


import urllib.request
import sys


def post_email(url, email):
    with urllib.request.urlopen(url, data=email.encode('utf-8')) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        url = sys.argv[1]
        email = sys.argv[2]
        post_email(url, email)
    else:
        print('Usage: ./2-post_email.py <url> <email>')
