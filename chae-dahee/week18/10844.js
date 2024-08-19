const input = require("fs").readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const dp = Array.from({ length: n + 1 }, () => new Array(10).fill(0));
const mod = Number(1e9);

dp[1][0] = 0;
for (let i = 1; i < 10; i++) {
  dp[1][i] = 1;
}

for (let i = 2; i <= n; i++) {
  for (let j = 0; j <= 9; j++) {
    dp[i][j] = 0;
    if (j > 0) dp[i][j] += dp[i - 1][j - 1];
    if (j < 9) dp[i][j] += dp[i - 1][j + 1];
    dp[i][j] %= mod;
  }
}

let result = 0;
for (let i = 0; i <= 9; i++) {
  result += dp[n][i];
  result %= mod;
}

console.log(result);
