let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");

const [N, M] = input.shift().split(" ");
arr = input[0].split(" ").map(Number).sort((a, b) => a - b);

let start = 0;
let end = arr[arr.length - 1];
let ans = Number.MIN_SAFE_INTEGER;

while (start <= end) {
  let mid = Math.floor((start + end) / 2);
  let sum = 0;

  for (let x of arr) {
    if (x > mid) sum += x - mid;
  }

  //sum > M 길경우 mid+1
  if (sum >= M) {
    if (mid > ans) ans = mid;
    start = mid + 1;
  } else end = mid - 1;
}

console.log(ans);