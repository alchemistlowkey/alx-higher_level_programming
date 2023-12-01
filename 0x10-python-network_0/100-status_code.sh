#!/bin/bash
# Bash script that send request to URL passed as arg & displays the status code
curl -so /dev/null -w "%{http_code}" "$1"
