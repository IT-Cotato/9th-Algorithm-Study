let input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [n, d] = input[0].split(" ").map(Number);

const graph = Array.from(Array(d + 1), () => []);
let dist = Array.from(Array(d + 1).fill(Infinity)); //dist[50]:10

for (let i = 0; i < n; i++) {
  const [start, end, w] = input[i + 1].split(" ").map(Number);
  if (end > d) continue;
  if (end - start <= w) continue;

  graph[start].push([end, w]);
} //graph[0]: [[50, 10], [50, 20]]

let prev = -1;
for (let i = 0; i <= d; i++) {
  if (i) prev = dist[i - 1];

  dist[i] = Math.min(dist[i], prev + 1);

  for (let [next, cost] of graph[i]) {
    if (dist[next] > dist[i] + cost) {
      dist[next] = dist[i] + cost;
    }
  }
}
console.log(dist[d]);
