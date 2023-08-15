#!/usr/bin/node
exports.esrever = (list) => {
  const reversedList = [];
  let i = list.length - 1;
  while (i >= 0) {
    reversedList.push(list[i]);
    i--;
  }
  return reversedList;
};
