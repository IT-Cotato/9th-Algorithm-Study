/**
 * BOJ 10026 적록색약 골드5
 * n * n 그리드 칸 R, G, B
 * 상하좌우 인접 -> 같은 구역
 * 적록색약 -> R, G 같은 색으로 봄
 * 일반인 -> R, G, B 각각 구분
 * n 주어지고
 * 그림 주어지고
 * 일반인 구역수 출력
 * 적록색약 구역 수 출력
 * 공백으로 구분
 *
 */
#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
int board[101][101];
int nView[101][101];
int rgView[101][101];
queue<pair<int, int> > Q;
queue<pair<int, int> > rgQ;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
int n;
bool nVis[101][101];
bool rgVis[101][101];
vector<pair<int, int> > section;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; j++) {
            char c;
            cin >> c;
            if (c == 'R') {
                nView[i][j] = 0;
                rgView[i][j] = 0;
            } else if (c == 'G') {
                nView[i][j] = 1;
                rgView[i][j] = 0;
            } else {
                nView[i][j] = 2;
                rgView[i][j] = 2;
            }

        }
    }

    int cnt = 0;
    int rgCnt = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if(!nVis[i][j]) {
                Q.push(make_pair(i, j));
                cnt++;
                nVis[i][j] = true;
                while (!Q.empty()) {
                    pair<int, int> cur = Q.front();
                    Q.pop();
                    for (int dir = 0; dir < 4; dir++) {
                        int nx = cur.X + dx[dir];
                        int ny = cur.Y + dy[dir];
                        if(nVis[nx][ny]) {
                            continue;
                        }
                        if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                            continue;
                        }
                        if (nView[nx][ny] == nView[cur.X][cur.Y]) {
                            Q.push(make_pair(nx, ny));
                            nVis[nx][ny] = true;
                        }
                    }
                }
            }
            if(!rgVis[i][j]) {
                rgQ.push(make_pair(i, j));
                rgCnt++;
                rgVis[i][j] = true;
                while (!rgQ.empty()) {
                    pair<int, int> cur = rgQ.front();
                    rgQ.pop();
                    for (int dir = 0; dir < 4; dir++) {
                        int nx = cur.X + dx[dir];
                        int ny = cur.Y + dy[dir];
                        if(rgVis[nx][ny]) {
                            continue;
                        }
                        if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                            continue;
                        }
                        if (rgView[nx][ny] == rgView[cur.X][cur.Y]) {
                            rgQ.push(make_pair(nx, ny));
                            rgVis[nx][ny] = true;
                        }
                    }
                }
            }
        }
    }
    cout << cnt << ' ' << rgCnt;

}