#include <bits/stdc++.h>
#define MAX 0x3f3f3f
using namespace std;

int vis[1003];
vector<pair<int, int> > v[1003];
void fc(int a){
    priority_queue<pair<int, int>, vector<pair<int,int> >, greater<pair<int, int> > > pq;
    pq.push(make_pair(0, a));
    vis[a] = 0; // 출발 도시 비용 = 0
    while (!pq.empty())
    {
        int cost = pq.top().first; // 현재 도시까지 비용
        int x = pq.top().second; // 현재 도시
        pq.pop();

        if (vis[x] < cost)
            continue;

        // x 도시와 이어진 도시들 검사
        for (int i = 0; i < v[x].size(); i++){
            int nx = v[x][i].first; // 다음 도시
            int ncost = cost+v[x][i].second; // 다음 도시까지 비용

            if (vis[nx] > ncost){
                pq.push(make_pair(ncost, nx));
                vis[nx] = ncost; // 비용 다시 기록
            }
        }
    }
}
int main(){
    int n, m;
    cin >> n >> m;

    v[0].push_back(make_pair(0, 0));
    memset(vis, MAX, sizeof(vis));
    for (int i = 0; i < m; i++){
        int a, b, c;
        cin >> a >> b >> c;
        v[a].push_back(make_pair(b, c));
    }
    int st, dt; // 출발 도시, 도착 도시
    cin >> st >> dt;
    fc(st);
    cout << vis[dt]; // dt 도시의 비용 출력
    return 0;
}