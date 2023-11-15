#!/usr/bin/node
exports.esrever = function (list) {
  const tmp = [];
  for (let i = list.length - 1; i >= 0; i--) {
    tmp.push(list[i]);
  }

  return tmp;
};
