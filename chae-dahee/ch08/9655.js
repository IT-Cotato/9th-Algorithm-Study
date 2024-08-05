const [n] =  require('fs').readFileSync('/dev/stdin').toString().split('\n');
console.log(n %2 === 0? 'CY':'SK');