#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const textFile = process.argv[3];

fs.writeFile(filePath, textFile, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
