#!/usr/bin/node
exports.nbOccurences = (list, searchElement) => {
  let count = 0;
  for (const element of list) {
    if (element === searchElement) {
      count++;
    }
  }
  return count;
};
