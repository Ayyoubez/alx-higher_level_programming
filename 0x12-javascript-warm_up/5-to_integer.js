#!/usr/bin/node

const args = process.argv;

const var1 = +(args[2]);
if (isNaN(var1)) {
  console.log('Not a number');
} else { console.log(`My number: ${args[2]}`); }
