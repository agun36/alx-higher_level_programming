#!/usr/bin/node
const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);

function add(a, b) {
  const output = arg1 + arg2;
  console.log(output);
}

add(arg1, arg2);
