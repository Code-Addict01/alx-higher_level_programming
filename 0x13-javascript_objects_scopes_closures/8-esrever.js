#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  for (let i = 0; (len - 1) > 0; i++) {
    const tmp = list[len];
    list[len] = list[i];
    list[i] = tmp;
    len--;
  }
  return list;
};
