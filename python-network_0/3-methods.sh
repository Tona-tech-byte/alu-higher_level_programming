#!/bin/bash
# Display all HTTP methods accepted by the server
curl -s -I -X OPTIONS "$1" | grep -i "^Allow:" | cut -d' ' -f2- | tr -d '\r'
