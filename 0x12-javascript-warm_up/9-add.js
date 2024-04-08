#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const a = process.argv;
add(Number(a[2]), Number(a[3]));
