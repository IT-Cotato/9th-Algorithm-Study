let input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const n = parseInt(input[0]);
const house = input[1].split(" ").map(Number)

function Antenna(house){
    // house.sort((a, b) => b-a);
    // return  position = house[Math.floor(house.length / 2)];

    house.sort((a, b) => a-b);
    const  position = Math.floor(house.length / 2);
    return house.length % 2 === 0? house[position-1] : house[position];
}

console.log(Antenna(house));