#include <bits/stdc++.h>
using namespace std;


/**
 * BOJ 2644 촌수 실버 2
 *
 * 전체 사람 수 n
 * 계산해야할 두 사람 a, b
 * 관계 m
 * 부모 x, 자식 y
 *
 */
int n, m, a, b;
int vis[101];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    vector<int> graph[101];

    cin >> n;
    cin >> a >> b;
    cin >> m;
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        graph[x].push_back(y);
        graph[y].push_back(x);
    }

    queue<int> q;
    q.push(a);
    vis[a] = true;
    int cnt = -1;
    while(!q.empty()) {
        cnt++; // 0으로 시작
        auto s = q.size();
        for (int i = 0; i < s; i++) {
            int cur = q.front();
            q.pop();
            if (cur == b) {
                cout << cnt;
                return 0;
            }
            for (auto v: graph[cur]) {
                if (vis[v]) {
                    continue;
                }

                q.push(v);
                vis[v] = true;
            }
        }
    }


    cout << -1;







}