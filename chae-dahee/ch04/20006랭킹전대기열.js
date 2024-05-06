// 입력 처리
const fs = require('fs');
const input = fs.readFileSync('chae-dahee/ch04/20006.txt').toString().trim().split('\n');
const [p, m] = input[0].split(' ').map(Number);
const players = input.slice(1).map(line => {
    const [level, name] = line.split(' ');
    return { level: Number(level), name };
});

function matching(p, m, players) {
    const rooms = [];
    const addPlayerToRoom = (room, player) => {
        room.players.push(player);
        if (room.players.length === room.capacity) {
            room.started = true;
        }
    };

    players.forEach(player => {
        let matched = false;
        rooms.forEach(room => {
            if (!room.started && Math.abs(room.players[0].level - player.level) <= 10 && room.players.length < m) {
                addPlayerToRoom(room, player);
                matched = true;
            }
        });
        if (!matched) {
            const room = {
                players: [player],
                capacity: m,
                started: false
            };
            rooms.push(room);
        }
    });

    rooms.forEach(room => {
        console.log(room.started ? "Started!" : "Waiting!");
        room.players.sort((a, b) => a.name.localeCompare(b.name));
        room.players.forEach(player => console.log(`${player.level} ${player.name}`));
    });
}



// 매칭 수행
matching(p, m, players);
