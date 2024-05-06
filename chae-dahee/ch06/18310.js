let input = require("fs").readFileSync('/dev/stdin').toString().trim().split("\n");

const n = parseInt(input[0]);
const house = input[1].split(" ").map(Number)

function Antenna(house){
    house.sort((a, b) => b-a);
    return  position = house[Math.floor(house.length / 2)];
}

console.log(Antenna(house));