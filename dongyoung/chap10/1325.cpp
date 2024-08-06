#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> trust[10001];
bool vis[10001];
vector<int> ans;

int bfs(int &x) { // x를 해킹했을 때 해킹할 수 있는 컴퓨터의 개수 리턴
    fill(vis, vis + 10001, false);
    int cnt = 0;
    queue<int> q;
    q.push(x);
    cnt++;
    vis[x] = true;
    while(!q.empty()) {
        int cur = q.front();
        q.pop();
        for (auto i: trust[cur]) {
            if (vis[i]) {
                continue;
            }
            q.push(i);
            vis[i] = true;
            cnt++;
        }
    }
    return cnt;
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        trust[b].push_back(a);
    }

    int mx = -1;
    for (int i = 1; i <= n; i++) {
        int result = bfs(i);
        if(result > mx) {
            mx = result;
            ans.clear();
            ans.push_back(i);
        } else if(result == mx) {
            ans.push_back(i);
        }
    }

    for (auto i: ans) {
        cout << i << ' ';
    }




}