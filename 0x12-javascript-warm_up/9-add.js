#!/usr/bin/node
function add(a, b) {
  let sum;
  sum = a + b;
  return sum;
}

const arg1 = parseInt(process.argv[2]);
const arg2 = parseInt(process.argv[3]);

if (!isNaN(arg1) && !isNaN(arg2)) {
  const result = add(arg1, arg2);
  console.log(result);
} else {
  console.log('NaN');
}

