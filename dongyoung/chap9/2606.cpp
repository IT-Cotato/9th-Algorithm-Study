#include <bits/stdc++.h>

using namespace std;
int com;
vector<int> network[101];
bool vis[101];
int result = 0;

void bfs(int n) {
    queue<int> q;
    q.push(n);
    vis[n] = true;
    while(!q.empty()) {
        int cur = q.front();
        q.pop();

        for (auto i: network[cur]) {
            if (vis[i]) {
                continue;
            }
            q.push(i);
            vis[i] = true;
            result++;
        }
    }

}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> com;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        network[a].push_back(b);
        network[b].push_back(a);
    }

    bfs(1);
    cout << result;


}