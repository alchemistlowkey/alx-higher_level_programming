#!/bin/bash
# Bash script that makes a request & causes server to respond "You got me"!
curl -sLX PUT -H "Origin:HolbertonSchool" -d "user_id=98" "0.0.0.0:5000/catch_me"
