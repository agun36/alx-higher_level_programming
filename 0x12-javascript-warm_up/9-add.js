#!/usr/bin/node
function add(a, b) {
  return a + b;
}

if (!isNaN(Number(process.argv[2])) && !isNaN(Number(process.argv[3]))) {
  const result = add(Number(process.argv[2]), Number(process.argv[3]));
  console.log(result);
} else {
  console.log('NaN');
}

