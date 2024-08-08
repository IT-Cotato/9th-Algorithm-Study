#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;

int n;
int arr[101][101];
bool vis[101][101];
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

int result;

int bfs(int h) { // 안전영역 개수 리턴

    queue<pair<int, int> > q;

    for (int i = 0; i < 101; i++) {
        fill(vis[i], vis[i] + 101, false);
    }
    vector<pair<int, int> > candidate;


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[i][j] > h) {
                candidate.push_back(make_pair(i, j));
            }
        }
    }
    int cnt = 0;

    for (auto x: candidate) {
        if (vis[x.X][x.Y]) {
            continue;
        }
        vis[x.X][x.Y] = true;
        q.push(x);

        cnt++;

        while (!q.empty()) {
            pair<int, int> cur = q.front();
            q.pop();

            for (int dir = 0; dir < 4; dir++) {
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];

                if (vis[nx][ny]) {
                    continue;
                }
                if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                    continue;
                }

                if (arr[nx][ny] > h) {
                    q.push(make_pair(nx, ny));
                    vis[nx][ny] = true;
                }

            }
        }
    }

    return cnt;
}


int main() {

    ios::sync_with_stdio(0);
    cin.tie();

    cin >> n;
    int mx = -1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
            mx = max(mx, arr[i][j]);
        }
    }

    for (int i = 0; i <= mx; i++) {
        result = max(result, bfs(i));
    }

    cout << result;


}