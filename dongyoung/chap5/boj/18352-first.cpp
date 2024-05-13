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

int n, m, k, x;
int dist[300002]; // 도착 지점 부터 거리
vector<int> to[300002]; // [x] : x로 가는 엣지의 출발지점을 담는 벡터
queue<int> Q; // bfs를 위한 queue
vector<int> ans; // 답 저장용
bool vis[300002];
bool isFirstVisit = true;


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m >> k >> x;

    for (int i = 1; i <= m; i++) {
        int a, b; // a -> b
        cin >> a >> b;
        to[b].push_back(a);
    }


    /**
     * 도착지가 1~n 인 상황 가정
     * 도착지부터 k 거리 만큼 떨어진 곳에 x가 있는지 확인하는 과정
     * 한 번 간 곳은 가면 안 됨
     */
    for (int i = 1; i <= n; i++) {

        fill(vis + 1, vis + n, false); // 방문 정보 초기화
        isFirstVisit = true;
        int hopCount = 1; // 거리
        if (i == x) {
            continue;
        } // 출발지가 자기 자신이면 건너뜀

        Q.push(i);
        vis[i] = true;

        /**
         * 큐가 비어있음: 더 이상 연결된 엣지가 없음
         * 이미 k 번을 움직였는데 x 가 없음 -> 답 아님
         * k 번을 움직이지 않았는데 x를 만남 -> 최소 거리가 아님
         */
        while(!Q.empty() && isFirstVisit) {
            int cur = Q.front();
            Q.pop();
            for (auto iter: to[cur]) { // i로 가는 모든 엣지 순회
                int from = iter;
                if (from == x) { // 출발지점이 x인 지점이 k 번 이내에 존재 -> 최소거리가 k가 아님
                    if (hopCount < k) {
                        isFirstVisit = false;
                    } else if (hopCount == k) {
                        ans.push_back(i); // 도착지점 i를 정답에 추가 
                    }
                    while (!Q.empty()) {
                        Q.pop(); // 이 도착지점은 이제 끝이니까 큐 초기화
                    }
                    break;
                }
                if (vis[from]) {
                    continue; // 이미 방문한 지점 건너뜀
                }
                Q.push(iter);
                vis[iter] = true;
                hopCount++;
                if (hopCount > k) {
                    while (!Q.empty()) {
                        Q.pop();
                    }
                    break;
                }
            }
        }

    }
    if (ans.empty()) {
        cout << -1 << '\n';
        return 0;
    }
    for (auto i: ans) {
        cout << i << '\n';
    }
}