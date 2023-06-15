#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const convert = parseInt(argv[2]);

if (isNaN(convert)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${convert}`);
}
