const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const N = +input[0];
const A = input[1].split(" ").map(Number);
let [i, j, min, output] = [0, N - 1, Infinity, ""];
while (i < j) {
  const sum = A[i] + A[j];
  if (Math.abs(sum) < min) {
    min = Math.abs(sum);
    output = `${A[i]} ${A[j]}`;
  }
  sum < 0 ? i++ : j--;
}
console.log(output);
