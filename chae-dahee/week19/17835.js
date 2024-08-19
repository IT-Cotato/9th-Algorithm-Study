const input = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n");

const [N, M, K] = input[0].split(" ").map(Number);
const arr = Array.from({ length: N + 1 }, () => []);
for (let i = 1; i <= M; i++) {
  const [a, b, cost] = input[i].split(" ").map(Number);
  arr[b].push([a, cost]);
}

const targets = input[M + 1].split(" ").map(Number);
const result = Array(N + 1).fill(Infinity);

const dijkstra = () => {
  const h = [];

  for (const t of targets) {
    h.push([0, t]);
    result[t] = 0;
  }
  h.sort((a, b) => a[0] - b[0]);

  while (h.length) {
    const [cost, city] = h.shift();
    if (result[city] < cost) continue;
    for (const [nextCity, nextCost] of arr[city]) {
      const newCost = cost + nextCost;
      if (newCost < result[nextCity]) {
        result[nextCity] = newCost;
        h.push([newCost, nextCity]);
        h.sort((a, b) => a[0] - b[0]);
      }
    }
  }
};

let maxStart = 0;
let maxCost = 0;
dijkstra();

for (let i = 1; i <= N; i++) {
  const r = result[i];
  if (r > maxCost && r !== Infinity) {
    maxStart = i;
    maxCost = r;
  }
}

console.log(maxStart);
console.log(maxCost);
