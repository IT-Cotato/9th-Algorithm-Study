let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const testCase = Number(input.shift());
let M, N, K, graph;

// DFS 탐색
const dfs = (x, y) => {
  const stack = [[x, y]];
  const dx = [-1, 1, 0, 0]; // 좌,우,상,하 x좌표 탐색
  const dy = [0, 0, 1, -1]; // 좌,우,상,하 y좌표 탐색

  while (stack.length) {
    const [curX, curY] = stack.pop();

	// 현재 위치에서 인접한(좌우상하) 곳에 배추 심어져있는지 확인
    for (let i = 0; i < 4; i++) {
      const nx = curX + dx[i];
      const ny = curY + dy[i];
			
	  // 현재 좌표가 밭을 벗어나지 않고, 인접한 곳에 배추가 심어져있는 경우
      if (nx >= 0 && nx < N && ny >= 0 && ny < M && graph[nx][ny]) {
        stack.push([nx, ny]);
        graph[nx][ny] = 0; // 현재 위치 방문 처리
      }
    }
  }
};

// 필요한 지렁이 마리 수 체크하는 함수
const howManyWorms = () => {
  let answer = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      if (graph[i][j]) {
        answer++;
        dfs(i, j);
      }
    }
  }
  console.log(answer);
};

for (let i = 0; i < testCase; i++) {
  // [가로길이, 세로길이, 배추가 심어져 있는 위치의 개수]
  [M, N, K] = input.shift().split(' ').map(Number);

  // 밭 크기와 동일한 그래프(초기값 0으로 채워진 2차원 배열) 생성
  graph = Array.from(Array(N), () => Array(M).fill(0));

  // 배추 위치 입력값받아 배추있는 자리에 1로 표시
  for (let j = 0; j < K; j++) {
    const [x, y] = input[j].split(' ').map(Number);
    graph[y][x] = 1;
  }

  // 필요한 지렁이 마리 수 출력하는 함수 호출
  howManyWorms();

  // 첫 번째 예제 출력값 호출 후, 다음 케이스로 넘어가기
  input = input.slice(K);
}