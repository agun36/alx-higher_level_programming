#!/usr/bin/node
let num = 0;
const x = Number(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  while (num < x) {
    console.log('C is fun');
    num++;
  }
}
