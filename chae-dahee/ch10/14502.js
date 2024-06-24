const [N, ...map] = require("fs")
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split("\n")
  .map((v) => v.split(" ").map(Number));

const [H, W] = N;
const dist = [
  [0, 1],
  [0, -1],
  [1, 0],
  [-1, 0],
];

const space = [];
const virus = [];
const answer = [];


for (let i = 0; i < H; i++) {
  for (let j = 0; j < W; j++) {
    if (map[i][j] == 0) {
      space.push([i, j]);
    } else if (map[i][j] == 2) {
      virus.push([i, j]);
    }
  }
}
const SPACE = space.length - 3;

for (let i = 0; i < space.length; i++) {
  for (let j = i + 1; j < space.length; j++) {
    for (let k = j + 1; k < space.length; k++) {
      let tempMap = JSON.parse(JSON.stringify(map));
      const [a, b] = space[i];
      const [c, d] = space[j];
      const [e, f] = space[k];

      tempMap[a][b] = 1;
      tempMap[c][d] = 1;
      tempMap[e][f] = 1;

      let v = 0;
      const tempVirus = JSON.parse(JSON.stringify(virus));
      while (tempVirus.length > 0) {
        const [vx, vy] = tempVirus.shift();
        dist.forEach((d) => {
          const nextX = vx + d[0];
          const nextY = vy + d[1];
          if (
            nextX >= 0 &&
            nextY >= 0 &&
            nextX < H &&
            nextY < W &&
            tempMap[nextX][nextY] == 0
          ) {
            tempMap[nextX][nextY] = 2;
            v++;
            tempVirus.push([nextX, nextY]);
          }
        });
      }
      answer.push(SPACE - v);
    }
  }
}

console.log(Math.max(...answer));
