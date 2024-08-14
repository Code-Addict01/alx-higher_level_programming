#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let Occurences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      Occurences++;
    }
  }
  return Occurences;
};
