#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || isNaN(w) || h <= 0 || isNaN(h)) {
      return {};
    }

    this.width = w;
    this.height = h;
  }

  print() {
    let num = 0;
    while (num < this.height) {
      console.log('X'.repeat(this.width));
      num++;
    }
  }

  rotate() {
    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    this.width *= 2;
    this.height *= 2;
  }
}
