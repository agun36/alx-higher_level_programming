#!/usr/bin/python3

"""
This Python script takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8).

Usage: ./2-post_email.py <url> <email>
"""


from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value)
    data = data.encode("ascii")

    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
