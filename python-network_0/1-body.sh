#!/bin/bash
# Display the response body only when the HTTP status is 200
body=$(mktemp); status=$(curl -s -L -o "$body" -w "%{http_code}" "$1"); [ "$status" = "200" ] && cat "$body"; rm -f "$body"
