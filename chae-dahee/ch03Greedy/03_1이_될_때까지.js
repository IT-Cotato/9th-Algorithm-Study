let fs = require('fs');
let input = fs.readFileSync('chae-dahee/ch03Greedy/03input.txt').toString().trim();

let [n,k] = input.split(' ').map(v => +v);

//방법1
function solution(n, k){
    let cnt = 0;
    
    while(n>1){
        n % k === 0? n /= k : n--;
    //   if(n % k === 0){
    //     n /= k;
    //   } else{
    //     n--;
    //   }
      cnt++;
    }
    
    return cnt;
  }
  
  console.log(solution(n, k));

// //방법2
// function solution(n,k){
//     let cnt = 0;

//     while(true){
//       let target = Math.floor(n/k)*k;
//       cnt += n-target;
//       n = target;
  
//       if(n < k)
//         break;

//       n = n/k;
//       cnt++;
//     }

//     cnt= cnt+(n-1);
//     return cnt;
//   }

//   console.log(solution(n,k));
