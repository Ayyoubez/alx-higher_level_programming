#!/usr/bin/node

function factorial (n) {
  if (isNaN(n)) { return 1; }
  if (n === 0) { return 1; }
  return (n * (factorial(n - 1)));
}
const a = process.argv;

console.log(factorial(a[2]));
