#!/usr/bin/node
const SquareBase = require('./5-square');

module.exports = class Square extends SquareBase {
  charPrint(c) {
    if (c === undefined) {
      c = 'X';
    };
    // methhod that print rectangle with while loop
    let num = 0;
    while (num < this.height) {
      console.log(c.repeat(this.width));
      num++;
    };
  };
};
