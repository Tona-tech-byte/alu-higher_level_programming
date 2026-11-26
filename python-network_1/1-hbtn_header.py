#!/usr/bin/python3
"""Fetch a URL and display its X-Request-Id response header."""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get("X-Request-Id"))
