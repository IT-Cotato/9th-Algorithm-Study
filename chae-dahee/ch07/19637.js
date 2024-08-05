const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(/\s+/);
const n = parseInt(input[0]);
const m = parseInt(input[1]);
const menu = [];

for (let i = 0; i < n; i++) {
  const name = input[2 + i * 2];
  const power = parseInt(input[3 + i * 2]);
  menu.push([name, power]);
}
menu.sort((a, b) => a[1] - b[1]);

const results = [];
for (let j = 0; j < m; j++) {
  const tempPower = parseInt(input[2 + n * 2 + j]);
  let start = 0;
  let end = menu.length - 1;

  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    if (tempPower > menu[mid][1]) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  results.push(menu[start][0]);
}
console.log(results.join("\n"));
