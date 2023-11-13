#!/usr/bin/node
if (process.argv[1] && process.argv[2] && process.argv[3]) {
  console.log('Arguments found');
} else if (process.argv[1] && process.argv[2]) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
