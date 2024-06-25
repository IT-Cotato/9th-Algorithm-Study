const input = require("fs")
  .readFileSync("chae-dahee/ch03Greedy/1080.txt")
  .toString()
  .trim()
  .split("\n");
const [N, M] = input.shift().split(" ").map(Number);
const A = input.slice(0, N).map((item) => item.split("").map(Number));
const B = input.slice(N, N * 2).map((item) => item.split("").map(Number));

function solution(N, M, A, B) {
  let cnt = 0;
  for (let i = 0; i < N - 2; i++) {
    for (let j = 0; j < M - 2; j++) {
      if (A[i][j] !== B[i][j]) {
        flip(i, j);
        cnt++;
      }
    }
  }
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (A[i][j] !== B[i][j]) {
        cnt = -1;
      }
    }
  }
  return cnt;
}
function flip(x, y) {
  for (let i = x; i < x + 3; i++) {
    for (let j = y; j < y + 3; j++) {
      A[i][j] = 1 - A[i][j];
    }
  }
}
console.log(solution(N, M, A, B));