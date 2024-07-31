const [N, K] = require("fs")
  .readFileSync("chae-dahee/ch05/12851.txt")
  .toString()
  .trim()
  .split(" ")
  .map((n) => Number(n));

const isVisited = new Array(100001).fill(false);
let p = 0;
const queue = [[N, 0]];

let minTime = Infinity;

while (p < queue.length) {
  const [loc, time] = queue[p];
  isVisited[loc] = true;
  if (loc === K) {
    minTime = time;
    break;
  }

  if (loc - 1 >= 0 && !isVisited[loc - 1]) {
    queue.push([loc - 1, time + 1]);
  }
  if (loc + 1 <= 100000 && !isVisited[loc + 1]) {
    queue.push([loc + 1, time + 1]);
  }
  if (2 * loc <= 100000 && !isVisited[2 * loc]) {
    queue.push([2 * loc, time + 1]);
  }
  p++;
}

let cnt = 0;
for (let i = p; i < queue.length; i++) {
  const [loc, time] = queue[i];
  if (loc === K && time === minTime) cnt++;
}

console.log(minTime + "\n" + cnt);
