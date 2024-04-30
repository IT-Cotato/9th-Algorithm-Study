let fs = require('fs');
let input = fs.readFileSync('chae-dahee/ch04/01input.txt').toString().trim();

const x = input.charCodeAt(0)-97+1;
const y = +input[1];

function isSafe(x,y){
    if(x<1 || x>8 || y<1 || y>8) return false;
    else return true;
}

function solution(x,y) {
    const dir=[//나이트가 이동할 수 있는 8가지 방향
        [-1,-2],[1,-2],[2,-1],[2,1],
        [1,2],[-1,2],[-2,1],[-2,-1]
    ]

    let cnt = 0;
    for(let i=0; i<8; i++) {
        const newx = x+dir[i][0];
        const newy = y+dir[i][1];

        if(isSafe(newx, newy))
        cnt++;
    }
    return cnt;
}

console.log(solution(x,y));