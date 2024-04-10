#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let c = 0;
  for (const e of list) {
    if (e === searchElement) {
      c++;
    }
  }
  return c;
};
