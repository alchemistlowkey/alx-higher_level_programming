#!/bin/bash
# Bash script that takes in a URL, sends a POST request and displays the body
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
