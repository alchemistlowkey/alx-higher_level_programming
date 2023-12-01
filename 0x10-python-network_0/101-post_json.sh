#!/bin/bash
# Bash script that sends JSON POST request as 1st arg & displays the body
curl -sH "Content-Type: application/json" -d @"$2" -X POST "$1"
