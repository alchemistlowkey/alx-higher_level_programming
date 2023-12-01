#!/bin/bash
# Bash script that takes a URL, display all HTTP methods the server will accept
curl -sIX OPTIONS "$1" | grep Allow | cut -f2 -d' '
