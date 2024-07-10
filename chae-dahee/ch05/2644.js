let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input.shift()); // 전체 사람 수
const [a, b] = input.shift().split(' ').map(Number); // a, b 두 사람의 번호
const m = Number(input.shift()); // 관계의 개수
const arr = input.map((v) => v.split(' ').map(Number)); // 부모-자식 관계 배열

let visited = Array(n + 1).fill(false);
let graph = [...Array(n + 1)].map(() => []);

// 양방향 그래프 만들기
arr.map(([from, to]) => {
  graph[from].push(to);
  graph[to].push(from);
});

// DFS
const dfs = (start, target) => {
  // stack 초기값 설정
  let stack = [[start, 0]];

  // 방문 처리
  visited[start] = true;

  while (stack.length) {
    const [curNum, depth] = stack.pop();

    if (curNum === target) return depth;

    for (const node of graph[curNum]) {
      if (!visited[node]) {
        visited[node] = true;
        stack.push([node, depth + 1]);
      }
    }
  }
  return -1;
};

console.log(dfs(a, b));