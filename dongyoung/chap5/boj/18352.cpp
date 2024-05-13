/**
* BOJ 18352 특정 거리의 도시 찾기 실버 2
 * n개의 노드, m개의 엣지 단방향 그래프
 * 모든 거리 1
 * 도시 x로 부터 출발해서 최단 거리가 k인 모든 도시의 번호 출력
 *
 * 첫 줄에 n, m, k, x -> 노드 개수, 엣지 개수, 거리 정보, 출발 도시
 * 2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
 * 자연수 a -> b m줄에 걸쳐 엣지 알려줌
 * 최단거리 k인 노드 오름차순 출력
*/

#include <bits/stdc++.h>
using namespace std;
vector<int> v[300002];
vector<int> ans;
queue<int> Q;
bool vis[300002];
int n, m, k, x;
int hopCount[300002]; // 출발지점에서 인덱스 까지 얼마나 떨어져있는지

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m >> k >> x;

    for (int i = 1; i <= m; i++) {
        int a, b; // a -> b
        cin >> a >> b;
        v[a].push_back(b); // a -> b
    }

    Q.push(x);
    vis[x] = true;
    hopCount[x] = 0; // 자기 자신으로 부터 0만큼 떨어져있음

    while(!Q.empty()) {
        int cur = Q.front(); // 이번에 방문한 도시
        Q.pop();
        for (auto i: v[cur]) { // 거기로 부터 갈 수 있는 도시 순회
            if (vis[i]) {
                continue;
            }
            if (hopCount[cur] == k-1) {
                ans.push_back(i);
                vis[i] = true;
                continue;
            }
            Q.push(i);
            vis[i] = true;
            hopCount[i] = hopCount[cur] + 1;
        }
    }
    if (ans.empty()) {
        cout << -1;
        return 0;
    }
    sort(ans.begin(), ans.end());
    for (int i: ans) {
        cout << i << '\n';
    }
}