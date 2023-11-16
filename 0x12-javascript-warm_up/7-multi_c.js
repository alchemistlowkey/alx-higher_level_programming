#!/usr/bin/node
const value = parseInt(process.argv[2]);
if (value) {
  for (let i = 0; i < value; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
