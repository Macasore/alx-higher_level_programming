#!/usr/bin/node
const process = require('process');
const argv = process.argv;
const x = parseInt(argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(x); i++) {
    let square = '';
    for (let j = 0; j < parseInt(x); j++) {
      square += 'X';
    }
    console.log(square);
  }
}
