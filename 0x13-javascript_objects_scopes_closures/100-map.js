#!/usr/bin/node

const { list } = require('./100-data');

const newList = list.map((num, index) => {
  return num * index;
});

console.log(list);
console.log(newList);
