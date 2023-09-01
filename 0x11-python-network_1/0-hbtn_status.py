#!/usr/bin/python3

import urllib.request

def hbtn_status():
  with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()

  print('Body response:')
  print('- type:', type(body))
  print('- content:', repr(body))
  print('- utf8 content:', body.decode('utf-8'))

if __name__ == "__main__":
  hbtn_status()
