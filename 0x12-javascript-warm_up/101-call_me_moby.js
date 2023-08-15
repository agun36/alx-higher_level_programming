#!/usr/bin/node
module.exports = {
  callMeMoby: function (n, f) {
    let i = 0;
    while (i < n;) {
      f();
      i++;
    };
  };
};
