#!/usr/bin/node

function add(a, b) {
  const arg1 = Number(a);
  const arg2 = Number(b);

  if (!isNaN(arg1) && !isNaN(arg2)) {
    return arg1 + arg2;
  } else {
    return 'NaN';
  }
}

console.log(add(process.argv[2], process.argv[3]));
