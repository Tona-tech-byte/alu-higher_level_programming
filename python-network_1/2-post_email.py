#!/usr/bin/python3
"""Send an email using a POST request."""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values).encode('utf-8')

    request = urllib.request.Request(sys.argv[1], data=data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
