#!/usr/bin/node

const { dict } = require('./101-data');

const newUser = {};

for (const key in dict) {
  const value = dict[key];
  if (!newUser[value]) {
    newUser[value] = [];
  }
  newUser[value].push(key);
}

console.log(newUser);
