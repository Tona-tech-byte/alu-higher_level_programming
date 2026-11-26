#!/bin/bash
# Send a GET request with the required custom headers
curl -s -H "X-HolbertonSchool-User-Id: 98" -H "X-School-User-Id: 98" "$1"
