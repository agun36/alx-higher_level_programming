#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
<<<<<<< HEAD
};  
=======
};
>>>>>>> b1c98422a1eda28c72ac987572628469c3a2ad77
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
