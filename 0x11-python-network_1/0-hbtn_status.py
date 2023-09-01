#!/usr/bin/python3

"""
This Python script fetches https://alx-intranet.hbtn.io/status
and prints the type, content, and UTF-8 content of the response.
"""

import urllib.request

def hbtn_status():
  """
  This function fetches the status of the HTB intranet and prints
  the type, content, and UTF-8 content of the response.

  Args:
    None

  Returns:
    None
  """

  with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
      body = response.read()
  print('Body response:')
  print('\t- type: {}'.format(type(body)))
  print('\t- content: {}'.format(body))
  print('\t- utf8 content: {}'.format(body.decode('utf-8')))

if __name__ == "__main__":
  hbtn_status()
