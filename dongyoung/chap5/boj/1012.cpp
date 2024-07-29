#include <bits/stdc++.h>
#define X first
#define Y second

using namespace std;

int t, m, n, k;
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
bool vis[51][51];
int board[51][51];

void bfs(int x, int y) {

    queue<pair<int, int> > q;

    q.push(make_pair(x, y));
    while(!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();

        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                continue;
            }

            if(vis[nx][ny]) {
                continue;
            }

            if (board[nx][ny] == 1) { // 배추 있는 곳
                q.push(make_pair(nx, ny));
                vis[nx][ny] = true;
            }
        }
    }
}
int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    while (t--) {
        int wormCnt = 0;

        for (int i = 0; i < 51; i++) {
            fill(board[i], board[i] + 51, 0);
        }

        for (int i = 0; i < 51; i++) {
            fill(vis[i], vis[i] + 51, false);
        }


        vector<pair<int, int> > cabbage; // 배추 위치 저장할 배열
        cin >> m >> n >> k;
        for (int i = 0; i < k; i++) {
            int x, y;
            cin >> y >> x; // 가로, 세로
            board[x][y] = 1;
            cabbage.push_back(make_pair(x, y));
        }

        for (auto cab: cabbage) {
            if (vis[cab.X][cab.Y]) {
                continue;
            } else {
                bfs(cab.X, cab.Y);
                wormCnt++;
            }
        }
        cout << wormCnt << '\n';

    }

}