#!/bin/bash
# Bash script that takes a URL, display all HTTP methods the server will accept
curl -sI "$1" | grep Allow | cut -f2 -d' '
