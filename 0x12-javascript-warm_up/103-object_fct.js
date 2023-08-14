const myObject = {
  type: 'object',
  value: 12,
  incr() {
    myObject.value++;
  }
};

console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
