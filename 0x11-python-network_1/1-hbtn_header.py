#!/usr/bin/python3

import urllib.request
import sys

def hbtn_header(url):
  with urllib.request.urlopen(url) as response:
    header = response.headers
    request_id = header['X-Request-Id']

  print(request_id)

if __name__ == "__main__":
  if len(sys.argv) == 2:
    url = sys.argv[1]
    hbtn_header(url)
  else:
    print('Usage: ./1-hbtn_header.py <url>')
