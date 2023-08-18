#!/usr/bin/node
let num = 0;
const x = Number(process.argv[2]);

if (!isNaN(x)) {
  while (num < x) {
    console.log('X'.repeat(x));
    num++;
  }
} else {
  console.log('Missing size');
}
