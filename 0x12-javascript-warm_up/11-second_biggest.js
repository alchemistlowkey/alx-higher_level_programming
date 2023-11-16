#!/usr/bin/node
const ac = process.argv.length;
const av = process.argv;
if (ac < 4) {
  console.log(0);
} else {
  const array = av.slice(2).sort((a, b) => a - b).reverse();
  console.log(array[1]);
}
