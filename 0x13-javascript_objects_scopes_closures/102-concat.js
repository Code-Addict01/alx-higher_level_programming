#!/usr/bin/node
const { readFileSync,  writeFile } = require('fs');
const { argv } = require('process');

const getContent = (file) => {
  return readFileSync(file, 'utf8');
};

const concatstr = getContent(argv[2]) + '' + getContent(argv[3]);

writeFile(argv[4], concatstr, 'utf8', err => {
  if (err) throw err;
});
