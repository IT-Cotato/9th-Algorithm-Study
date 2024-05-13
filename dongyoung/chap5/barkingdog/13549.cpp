/**
 * BOJ 13549 숨바꼭질 3 골드 5
 * 수빈이의 위치 N
 * 동생의 위치 K
 * 수빈이의 위치 이동 x -> x + 1 || x - 1
 * 순간이동 0초 후에 2 * x로 이동
 * N, K 주어짐
 * 수빈이가 동생을 찾는 가장 빠른 시간 출력
 *
 */

#include <bits/stdc++.h>
#define MAX_SIZE 100000 + 1
using namespace std;

int n, k;
deque<int> location;
int vis[MAX_SIZE];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> k;
    location.push_back(n);
    vis[n] = 1;
    while(!location.empty()){
        int cur = location.front();
        location.pop_front();
        if (cur == k) {
            cout <<  vis[cur] - 1;
            return 0;
        }
        if(cur * 2 < MAX_SIZE && !vis[cur * 2]) {
            location.push_front(cur * 2);
            vis[cur * 2] = vis[cur];
        }

        if (cur + 1 < MAX_SIZE && !vis[cur + 1]) {
            location.push_back(cur + 1);
            vis[cur + 1] = vis[cur] + 1;
        }

        if (cur -1 >= 0 && !vis[cur - 1]) {
            location.push_back(cur - 1);
            vis[cur - 1] = vis[cur] + 1;
        }
    }
}