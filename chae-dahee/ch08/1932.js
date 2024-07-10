const input = require("fs")
  .readFileSync("chae-dahee/ch08/1932.txt")
  .toString()
  .trim()
  .split("\n");
const n = parseInt(input[0]); // 삼각형 높이

const p = new Array(n).fill().map(() => []); // 입력 삼각형 값들과 dp 배열로 사용하기 위한 2차원 배열

// 피라미드 만들기
for (let i = 1; i <= n; i++) {
  const curRow = input[i].split(" ").map(Number);
  p[i - 1].push(...curRow);
}

for (let i = 1; i < n; i++) {
  // 가로 변
  for (let j = 0; j < p[i].length; j++) {
    // 단위 개수
    if (j === 0) {
      // 제일 왼쪽
      p[i][j] = p[i - 1][j] + p[i][j];
    } else if (j === p[i].length - 1) {
      // 제일 오른쪽
      p[i][j] = p[i - 1][j - 1] + p[i][j];
    } // 그 외
    else p[i][j] = Math.max(p[i - 1][j - 1], p[i - 1][j]) + p[i][j];
  }
}

console.log(Math.max(...p[n - 1]));
