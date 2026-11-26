#!/usr/bin/python3
"""Display the value of the X-Request-Id header."""
import sys
import requests


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
