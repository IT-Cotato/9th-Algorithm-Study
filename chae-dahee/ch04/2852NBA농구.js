let [N,...input] = require('fs').readFileSync('chae-dahee/ch04/2852.txt').toString().trim().split('\n');

let one = 0;
let two = 0;
const score = [];
let ans = [0,0];

input.forEach(v=>{
    const [team,t] = v.split(' ');
    const [mm,ss] = t.split(':');
    
    team==1? one++ : two++;

    const time = Number(mm) * 60 + Number(ss);

    if (one > two) score.push([1, time])
    else if (two > one) score.push([2, time])
    else score.push([0, time])
})

score.push([0, 2880])

for (let i = 1; i < score.length; i++) {
    if (score[i - 1][0] != 0)
        ans[score[i - 1][0] - 1] += score[i][1] - score[i - 1][1];
  }

ans = ans.map(v => {
    const mm = String(Math.floor(v / 60)).padStart(2, '0')
    const ss = String(v % 60).padStart(2, '0');
    return `${mm}:${ss}`
  }).join('\n')

console.log(ans);