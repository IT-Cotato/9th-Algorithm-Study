const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");
const n = +input[0];
let graph = Array.from({ length: n + 1 }, () => new Array());
let i = 1;
while (i < input.length - 1) {
  const [u, v] = input[i].split(" ").map(Number);
  graph[u].push(v);
  graph[v].push(u);
  i++;
}
let min = 51;
let idxGraph = [[]];
for (let i = 1; i <= n; i++) {
  let queue = [];
  let visited = Array(n + 1).fill(0);
  visited[i] = 1;
  let relation = Array.from({ length: n }, () => new Array());
  for (let neighbor of graph[i]) {
    queue.push([neighbor, 0]);
    visited[neighbor] = 1;
  }
  let max = 0;
  while (queue.length) {
    const [neighbor, dis] = queue.shift();
    max = dis;
    relation[dis].push(neighbor);
    for (let friend of graph[neighbor]) {
      if (visited[friend] === 0) {
        visited[friend] = 1;
        queue.push([friend, dis + 1]);
      }
    }
  }
  relation = relation.slice(0, max + 1);
  idxGraph.push(relation);
  min = Math.min(min, relation.length);
}
let answer1 = `${min} `;
let answer2 = "";
let cnt = 0;
for (let i = 1; i <= n; i++) {
  if (idxGraph[i].length === min) {
    cnt++;
    answer2 += `${i} `;
  }
}
answer1 += `${cnt}`;
console.log(answer1);
console.log(answer2.trim());
