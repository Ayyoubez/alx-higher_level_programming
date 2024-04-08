#!/usr/bin/node

function factorial (n) {
  if (n === 0) { return 1; }
  return (n * (factorial(n - 1)));
}
const a = process.argv;

console.log(factorial(a[2]));
