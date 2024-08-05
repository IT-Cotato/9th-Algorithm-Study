let [n, ...arr] = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
const names = [];
arr = arr
  .map((i) => i.split(" ").map((j) => Number(j) || j))
  .sort((a, b) => {
    if (a[1] < b[1]) return 1;
    //국어점수 비교(내림차순)
    else if (a[1] > b[1]) return -1;
    else {
      if (a[2] > b[2]) return 1;
      //영어점수 비교(오름차순)
      else if (a[2] < b[2]) return -1;
      else {
        if (a[3] < b[3]) return 1;
        //수학점수 비교(내림차순)
        else if (a[3] > b[3]) return -1;
        else {
          if (a[0] > b[0]) return 1;
          //이름비교(오름차순)
          else if (a[0] < b[0]) return -1;
          else return 0;
        }
      }
    }
  });
arr.forEach((v) => names.push(v[0]));
console.log(names.join("\n"));
