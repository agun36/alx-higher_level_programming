#!/usr/bin/node
const dict = require('./101-data').dict;

const dict_new = {};
const keys = Object.keys(dict);
let i = 0;
while (i < keys.length) {
  const mail = keys[i];
  if (dict[mail] in dict_new) {
    dict_new[dict[mail]].push(mail);
  } else {
    dict_new[dict[mail]] = [mail];
  }
  i++;
}

console.log(dict_new);
