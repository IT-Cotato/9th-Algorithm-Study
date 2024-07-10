const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n,m,k,x] = input.shift().split(' ').map(Number);
const arr = input.map((v)=>v.split(' ').map(Number));
const graph = [...Array(n+1)].map(()=>[]);
const distance = Array(n+1).fill(0);
let ans = [];

arr.map(([from, to]) => graph[from].push(to));

const bfs = (start) => {
    const Queue = [start];
    distance[start] = 1;

    while (Queue.length) {
        const now = Queue.shift();
        if (distance[now] == k+1){
            ans.push(now);
            continue;
        }
        
        for (const next of graph[now]) {
            if (!distance[next]){
                Queue.push(next);
                distance[next] = distance[now] +1;
            }
        }
    }
};

bfs(x);

if (ans.length) ans = ans.sort((a, b) => a-b).join('\n');
else ans = -1;

console.log(ans);
