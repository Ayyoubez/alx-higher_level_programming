#!/usr/bin/node

function secondBig (array) {
  let num = 0;
  if (array.length === 2) {
    return num;
  } else if (array.length === 3) {
    return num;
  } else {
    const newArray = array.slice(2).sort();
    num = newArray[newArray.length - 2];
    return num;
  }
}

const a = process.argv;
console.log(secondBig(a));
