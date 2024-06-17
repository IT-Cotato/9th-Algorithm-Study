let input = require("fs")
  .readFileSync("chae-dahee/ch10/1446.txt")
  .toString()
  .trim()
  .split("\n");

const [n, d] = input[0].split(" ").map(Number);

const graph = Array.from(Array(d + 1), () => []);
let dist = Array.from(Array(d + 1).fill(Infinity));

for (let i = 0; i < n; i++) {
  const [start, end, w] = input[i + 1].split(" ").map(Number);
  if (end > d) continue;
  if (end - start <= w) continue;

  graph[start].push([end, w]);
}

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
