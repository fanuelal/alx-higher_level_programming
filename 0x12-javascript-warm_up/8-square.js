#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing size');
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log('X'.repeat(process.argv[2]));
}
