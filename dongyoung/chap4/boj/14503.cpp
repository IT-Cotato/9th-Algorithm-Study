/**
* BOJ 14503 로봇 청소기 골드 5
 *
*/

#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int n, m, r, c, d;
int board[51][51]; // 좌표
bool vis[51][51]; // 방문 여부 저장
int dx[4] = {-1, 0, 1, 0}; // 북 동 남 서
int dy[4] = {0, 1, 0, -1};

int visCnt; // 방문 횟수

void dfs() {
    for (int i = 0; i < 4; i++) {
        int nd = (d + 3 - i) % 4; // 반시계 방향 회전 90도
        int nx = r + dx[nd]; // 새로운 방향으로 한칸 전진 좌표
        int ny = c + dy[nd];

        if (board[nx][ny] == 1 || nx < 0 || nx >= n || ny < 0 || ny >= m) { // 전진 불가능
            continue;
        }

        // 전진 가능(방문한 적 없음)
        if (board[nx][ny] == 0 && vis[nx][ny] == 0) {
            visCnt++;
            r = nx;
            c = ny;
            d = nd;
            vis[nx][ny] = true;
            dfs();
        }
    }

    /**
     * 4방향 모두 확인했는데 여기로 왔다?
     * 더 이상 갈 길이 없음 -> 후진 시도
     */
    int backIdx = d > 1 ? d - 2 : d + 2; // 후진할 때의 인덱스 0 1 2 3 일때, 2 3 0 1
    int backX = r + dx[backIdx];
    int backY = c + dy[backIdx];

    // 방향은 그대로 보는 상태로 후진 가능 여부 확인
    if (backX >= 0 && backX < n || backY >= 0 && backY < m) {
        //후진을 할 수 있는 상태
        if (board[backX][backY] == 0) {
            r = backX;
            c = backY;
            dfs();
        } else { // 후진 불가능 -> 상황 종료
            cout << visCnt << '\n';
            exit(0);
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    cin >> r >> c >> d;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }

    visCnt = 1;
    vis[r][c] = true;

    dfs();
}