/**
 * 12 : 30 start
 * 13 : 30 end
 *
 * BOJ 12851 숨바꼭질 2 골드 4
 */
#include <bits/stdc++.h>

using namespace std;

int n, k;
pair<bool, int> vis[100001];  // { 점 도착 여부 , timeCnt }
//int vis[100001];
queue<int> q;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> k;

    if (n == k) { // 같은 곳에 있는 경우(예 : 0 0)
        cout << 0 << '\n' << 1;
        return 0;
    }
    q.push(n);
    vis[n] = make_pair(true, 0);
    int timeCnt = 0;
    int wayCnt = 0;
    bool isWayFound = false;
    while (!isWayFound) {
        auto qSize = q.size();
        timeCnt ++;
        for (int i = 0; i < qSize; i++) {
            int cur = q.front();
            q.pop();
            int ways[3] = {cur - 1, cur + 1, cur * 2};
            for (auto way: ways) {
                if (way < 0 || way > 100000) {
                    continue;
                }
                if (vis[way].first && vis[way].second != timeCnt) {
                    continue;
                }

                if (way == k) {
                    wayCnt++;
                    isWayFound = true;
                    continue;
                }

                q.push(way);
                vis[way] = make_pair(true, timeCnt);
            }
        }
    }
    cout << timeCnt << '\n' << wayCnt;
}