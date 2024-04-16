let input = require('fs').readFileSync('chae-dahee/ch04/80979.txt').toString().split('\n').map((val)=>val.trim());

function solution(input) {
    let [n,k] = input.shift().split(' ').map((v)=>+v);

    let country=[];
    let rank = 1;
    for (let i=0; i<n; i++){
        let temp = input.shift().split(' ').map((v)=>+v);
        country.push(temp);
    }

    country.sort((a,b)=>a[0]-b[0]);

    rank += country.filter((v)=>
    v[1] > country[k-1][1] ||
    (v[1] === country[k - 1][1] && v[2] > country[k - 1][2]) ||
      (v[1] === country[k - 1][1] && v[2] === country[k - 1][2] && v[3] > country[k - 1][3])
).length;

    console.log(rank);
}

solution(input);