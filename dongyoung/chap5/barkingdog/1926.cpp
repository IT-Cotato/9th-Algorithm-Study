/**
 * BOJ 1926 그림 실버 1
 * 1로 연결된 것을 그림
 *
 * 그림의 개수, 가장 넓은 그림의 넓이 출력(그림이 하나도 없으면 0)
 *
 * 1인 것들을 저장해두고.. 순회하면서 vis이면 안가고 안갔으면 거기서부터 bfs
 */

#include <bits/stdc++.h>
using namespace std;
#define X first
#define Y second

int board[502][502];
int n, m;
bool vis[502][502];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};
vector<int> picture; // 그림 정보

vector<pair<int, int > > one;
queue<pair<int ,int> > Q;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
            if (board[i][j] == 1) {
                one.push_back(make_pair(i, j));
            }
        }
    }

    int mx = -1, cnt = 0;
    for (auto i: one) {
        if(vis[i.first][i.second]) continue;
        int s = 0;
        Q.push(i);
        vis[i.first][i.second] = true;
        s++;
        while (!Q.empty()) {
            pair<int, int> cur = Q.front();
            Q.pop();
            vis[cur.first][cur.second] = true;
            for (int dir = 0; dir < 4; dir++) {
                int nx = cur.first + dx[dir];
                int ny = cur.second + dy[dir];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    continue;
                }
                if (vis[nx][ny]) {
                    continue;
                }
                if (board[nx][ny] == 1) {
                    Q.push(make_pair(nx, ny));
                    vis[nx][ny] = true;
                    s++; // 그림의 크기 ++
                }
            }
        }
        mx = max(mx, s);
        cnt++; // 그림 개수 ++
    }

    if (mx == -1) {
        mx = 0; // 그림이 하나도 없는 경우에 그림 크기 0으로 만들기
    }
    cout << cnt << '\n' << mx;


}