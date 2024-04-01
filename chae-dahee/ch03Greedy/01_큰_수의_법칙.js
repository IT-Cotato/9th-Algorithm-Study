let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [num,arr] = input;
let [n,m,k] = num.split(' ').map(v=>+v);
arr = arr.split(' ').map(v=>+v);

//방법 1
function solution(n, m, k, arr){
  arr.sort((a, b) => b - a);
  const first = arr[0];
  const second = arr[1];
  
  let result = 0;
  while(1){
    if(m === 0) break;
    
    result += first * k;
    m -= k;
  
    result += second;
    m--;
  }
  
  return result;
}

console.log(solution(n, m, k, arr));

// //방볍 2
// function solution(n, m, k, arr){
//   arr.sort((a, b) => b - a);
//   const first = arr[0];
//   const second = arr[1];
  
//   let result = 0;
//   for(let i = 0, tmp = 0; i < m; i++){
//     if(tmp === k){
//       result += second;
//       tmp = 0;
//     } else{
//       result += first;
//       tmp++; 
//     }
//   }
//   return result;
// }
// console.log(solution(n, m, k, arr));

// //방법 3
// function solution(n, m, k, arr){
//   arr.sort((a, b) => b - a);
//   const first = arr[0];
//   const second = arr[1];

//   //가장 큰 수가 더해지는 횟수
//   let count = Math.floor((m / (k + 1)) * k);
//   count += m % (k + 1);

//   let result = 0;
//   result += count * first;
//   result += (m - count) * second;
  
//   return result;
// }
// console.log(solution(n, m, k, arr));