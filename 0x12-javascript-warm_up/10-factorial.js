#!/usr/bin/node
const process = require('process');
const argv = process.argv;
argv[2] = parseInt(argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    return (1);
  } else if (n === 1) {
    return (1);
  } else {
    return (n * factorial(n - 1));
  }
}

console.log(factorial(argv[2]));
