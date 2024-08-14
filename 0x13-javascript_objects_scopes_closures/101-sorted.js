#!/usr/bin/node
const dict = require('./101-data').dict;
const dKeys = Object.keys(dict);
const values = Object.values(dict);
let matched;
const res = {};

for (let i = 0; i < values.length; i++) {
  res[JSON.stringify(values[i])] = [];
  matched = dKeys.filter(key => dict[key] === values[i]);
  matched.forEach(item => res[JSON.stringify(values[i])].push(item));
}
console.log(res);
