#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second
#define INF 0x3f3f3f3f

int v, e, k;
int d[20005];

vector<pair<int, int>> dist[20005]; // {거리, 정점}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> v >> e >> k;
    fill(d, d + v + 1, INF);

    for(int i = 0; i < e; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        dist[u].push_back({w, v});
    }

    d[k] = 0;

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    pq.push({d[k], k});
    while (!pq.empty()) {
        auto cur = pq.top(); pq.pop();

        if(d[cur.Y] != cur.X) continue;
        for(auto nxt : dist[cur.Y]) {
            if(d[nxt.Y] <= d[cur.Y] + nxt.X) continue;

            d[nxt.Y] = d[cur.Y] + nxt.X;
            pq.push({d[nxt.Y], nxt.Y});
        }
    }

    for (int i = 1; i <= v; i++) {
        if(d[i] == INF) cout << "INF\n";
        else cout << d[i] << '\n';
    }
}