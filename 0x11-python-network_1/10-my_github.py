#!/usr/bin/python3

"""
This Python script takes your GitHub credentials
(username and password) and usesthe GitHub API
to display your id.
You must use Basic Authentication with a personal
access token as password to access to your information
(only read:user permission is needed)
The first argument will be your username
The second argument will be your password
(in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other
than requests and sys You don’t need to check
arguments passed to the script (number or type)
"""


import requests as rq
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'

    try:
        r = rq.get(url, auth=(argv[1], argv[2]))
        print(r.json().get('id'))

    except KeyError:
        print('None')
