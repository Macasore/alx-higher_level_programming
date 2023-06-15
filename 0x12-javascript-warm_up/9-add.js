#!/usr/bin/node
const process = require('process');
const argv = process.argv;
argv[2] = parseInt(argv[2]);
argv[3] = parseInt(argv[3]);

function add (a, b) {
  return (a + b);
}

console.log(add(argv[2], argv[3]));
