const [info, ...input] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((item) => item.split(" ").map((value) => +value));

const [N, M] = info;

const solution = () => {
  const graph = Array.from({ length: N + 1 }, () => []);

  for (let i = 0; i < M; i++) {
    const [a, b] = input[i];
    graph[b].push(a);
  }

  let max = 0;
  let answer = [];

  const DFS = (n) => {
    let check = Array.from({ length: N + 1 }, () => 0);
    let count = 1; // 해킹된 컴퓨터 수
    let stack = [n]; // DFS 탐색 스택

    check[n] = 1;

    while (stack.length) {
      const value = stack.pop();
      for (let i = 0; i < graph[value].length; i++) {
        if (!check[graph[value][i]]) {
          count += 1;
          check[graph[value][i]] = 1;
          stack.push(graph[value][i]);
        }
      }
    }
    if (max > count) return;
    else if (max === count) answer.push(n);
    else {
      max = count;
      answer = [n];
    }
  };

  for (let i = 1; i <= N; i++) {
    DFS(i);
  }

  return answer.join(" ");
};

console.log(solution());
