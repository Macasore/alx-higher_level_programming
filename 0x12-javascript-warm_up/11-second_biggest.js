#!/usr/bin/node
const args = process.argv;

const numbers = args.slice(2);

if (numbers.length <= 1) {
  console.log(0);
} else {
  numbers.sort((a, b) => b - a);
  console.log(Number(numbers[1]));
}
