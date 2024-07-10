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

  //뒤집어야할 원소가 있는지
  for (let i = 0; i < N - 2; i++) { //3 x 3 부분 행렬이 전체 행렬을 넘어가면 안됨.
    for (let j = 0; j < M - 2; j++) {
      if (A[i][j] !== B[i][j]) {
        flip(i, j);
        cnt++;
      }
    }
  }

  //행렬 A와 B가 동일한지 > 아니면 -1출력
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (A[i][j] !== B[i][j]) {
        cnt = -1;
      }
    }
  }
  return cnt;
}

//원소 뒤집는 함수
function flip(x, y) {
  for (let i = x; i < x + 3; i++) { // 3 x 3 범위
    for (let j = y; j < y + 3; j++) {
      A[i][j] = 1 - A[i][j]; // 0 > 1 , 1 > 0
    }
  }
}
console.log(solution(N, M, A, B));