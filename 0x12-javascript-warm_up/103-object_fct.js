#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
incr = () => {
  return myObject.value++;
};

console.log(myObject);

incr();
console.log(myObject);
incr();
console.log(myObject);
incr();
console.log(myObject);
