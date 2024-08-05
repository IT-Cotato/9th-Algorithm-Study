#include <bits/stdc++.h>
using namespace std;

int n;
int graph[101][101];
bool result[101][101];

bool vis[101];

void bfs(int st, int en) {
    fill(vis, vis + n + 1, false);
    queue<int> q;
    q.push(st);
    vis[st] = true;
    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int i = 1; i <= n; i++) {
            if (graph[cur][i]) {
                if (i == en) {
                    result[st][en] = true;
                }
                if (vis[i]) {
                    continue;
                }
                q.push(i);
                vis[i] = true;
            }
        }
    }

}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> graph[i][j];
        }
    }


    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            bfs(i, j);
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << result[i][j] << ' ';
        }
        cout << '\n';
    }






}