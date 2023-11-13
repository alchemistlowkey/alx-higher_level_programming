#!/usr/bin/node
const value = parseInt(process.argv[2]);
if (value) {
  for (let i = 0; i < value; i++) {
    let row = '';
    for (let j = 0; j < value; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
