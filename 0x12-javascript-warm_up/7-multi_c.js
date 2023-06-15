#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const x = parseInt(argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
}
