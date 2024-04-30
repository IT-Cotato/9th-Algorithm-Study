let input = require('fs').readFileSync('chae-dahee/ch04/02input.txt').toString().trim().split('\n');

const [nm, abd, ...arr]=input;
const [n,m] = nm.split(' ').map(v=>+v);
let [x,y,d] = abd.split(' ').map(v=>+v);
const map = arr.map(v=>v.split(' ').map(v=>+v));

function solution(n,m,x,y,d,map){
    //방향
    const dir = [[0,-1], [1,0], [0,1], [-1,0]];
    //방문정보
    let visited = Array.from(Array(n), () => Array(m).fill(false));
    visited[x][y] = true;

    let cnt = 1;
    let turncnt = 0;

    while(1){
        d = d===0? 3 : d-1;
        let nx = x+dir[d][0];
        let ny = y+dir[d][1];

        //정면에 가보지 않은 칸이 존재하는 경우
        if(!map[nx][ny] && !visited[nx][ny]){
            visited[nx][ny] = true;
            x=nx;
            y=ny;
            cnt++;
            turncnt=0;
            continue;
        }else{//정면에서 가보지 않은 칸이 없거나, 바다인 경우
            turncnt++;
        }

        //네 방향 모두 갈 수 없는 경우
        if(turncnt === 4){
            nx = x-dir[d][0];
            ny = y-dir[d][1];

            //뒤로 갈 수 있으면 이동
            if(!map[nx][ny]){
                x=nx;
                y=ny;
                turncnt=0;
            }else{//뒤가 바다로 막혀있는 경우
                break;
            }
        }
    }
    
    return cnt;
}
console.log(solution(n,m,x,y,d,map));