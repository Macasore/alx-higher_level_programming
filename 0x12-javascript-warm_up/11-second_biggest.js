#!/usr/bin/node
const process = require('process');
const argv = process.argv;
let largest = 0;
let secLargest;

if (argv.length <= 2) {
  console.log(largest);
} else if (argv.length === 3) {
  console.log(largest);
} else {
  for (let i = 2; i < argv.length; i++) {
    const convert = parseInt(argv[i]);
    if (convert > largest) {
      secLargest = largest;
      largest = convert;
    } else {
      continue;
    }
  }
  console.log(secLargest);
}
