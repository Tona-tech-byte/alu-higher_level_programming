#!/bin/bash
# Send a request and display the response body size in bytes
curl -s "$1" | wc -c
