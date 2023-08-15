#!/usr/bin/node
// create new instance with constructor
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || isNaN(w) || h <= 0 || isNaN(h)) {
      return {};
    }
    this.width = w;
    this.height = h;
  }
  // methhod that print rectangle with while loop
  print() {
    let num = 0;
    while (num < this.height) {
      console.log('X'.repeat(this.width));
      num++;
    }
  } 
};
