#!/bin/bash
# Bash script that sends DELETE request to URL passed as 1st arg, displays body
curl -sX "DELETE" "$1"
