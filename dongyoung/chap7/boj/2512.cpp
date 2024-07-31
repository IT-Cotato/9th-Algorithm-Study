/**
 * [BOJ] 예산 / 7장 / 60분 / 실버 2
 */

#include <bits/stdc++.h>

using namespace std;

int n, m;
int budget[10001];

bool solve(int x) {
    int cur = 0;
    for (int i = 0; i < n; i++) {
        if (budget[i] < x) {
            cur += budget[i];
        } else {
            cur += x;
        }
    }

    return cur <= m; // 예산 초과 x : true, 초과 : false

}


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    int sum = 0;
    for (int i = 0; i < n; i++) {
        cin >> budget[i];
        sum += budget[i];
    }

    sort(budget, budget + n);
    cin >> m;

    int st = 0;
    int en = budget[n-1] + 1;
    while(st + 1 < en) {
        int mid = (st + en) / 2;
        if (solve(mid)) { // cur >= m (현재 mid 값으로 상한액을 설정했을 때 총액 <= 예산
            st = mid;
        } else {
            en = mid;
        }

    }
    cout << st;

}