#!/usr/bin/node
const [, , ...args] = process.argv;

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const nums = args.map(arg => parseInt(arg));
  const max1 = Math.max(...nums);
  nums.splice(nums.indexOf(max1), 1);
  const max2 = Math.max(...nums);
  console.log(max2);
}
