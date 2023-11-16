#!/usr/bin/node
function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

const value = parseInt(process.argv[2]);

if (value) {
  console.log(factorial(value));
} else {
  console.log(factorial(value));
}
