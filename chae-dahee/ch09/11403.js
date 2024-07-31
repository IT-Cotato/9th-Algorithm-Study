const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = +input[0];
const graph = input.slice(1).map(v => v.split(' ').map(Number));

const output = [...Array(N)].map(() => Array(N).fill(0));
const dfs = (node, start, visited) => {
  for (let i = 0; i < N; i++) {
    if (graph[node][i] && !visited[i]) {
      visited[i] = true;
      output[start][i] = 1;
      dfs(i, start, visited);
    }
  }
};

for (let i = 0; i < N; i++) {
  const visited = Array(N).fill(false);
  dfs(i, i, visited);
}

console.log(output.map(v => v.join(' ')).join('\n'));