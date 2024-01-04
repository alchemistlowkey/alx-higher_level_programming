#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

let count = 0;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    for (const data in JSON.parse(body).results) {
      for (const actor in JSON.parse(body).results[data].characters) {
        if (JSON.parse(body).results[data].characters[actor].includes('18')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
