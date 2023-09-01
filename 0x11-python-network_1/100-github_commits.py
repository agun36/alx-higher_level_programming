#!/usr/bin/python3

"""
The Holberton School staff evaluates candidates applying for a
back-end position with multiple technical challenges, like this one:
"""

import requests
from sys import argv


if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    res = requests.get(url)
    commits = res.json()
    for commit in commits[:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
