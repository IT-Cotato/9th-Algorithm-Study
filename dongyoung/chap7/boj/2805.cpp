/**
* BOJ 2805 나무 자르기 실버 2
 * 나무 m 미터 필요
 * 절단기 높이 h
 * 나무의 높이 h + x
 * -> x 만큼 잘림
 * 절단기 높이의 최댓값 구하기
*/

#include <bits/stdc++.h>
using namespace std;
int n, m;
int h[1000002]; //나무의 높이


/**
 * 절단기 높이가 x일 때 잘리는 나무의 길이 합이 m 이상이면 true를 리턴하는 함수
 * x가 커질수록 잘리는 나무의 길이 합은 감소
 * 이분탐색을 수행할 때 true이면
 */

bool solve(int x) {
    long long cur = 0; // 잘리는 나무의 길이 합(n개의 나무 * 나무의 길이m <= 1,000,000 * 2,000,000,000 = 2,000,000,000,000,000)
    for (int i = 0; i < n; i++) {
        if (h[i] <= x) { // 절단기보다 길이가 작거나 같은 나무는 안 잘림
            continue;
        }
        cur += h[i] - x;
    }
    return cur >= m;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> h[i]; // 나무의 높이
    }
    int st = 0;
    int en = *max_element(h, h + n);

    while (st < en) {
        int mid = (st + en + 1) / 2;
        if (solve(mid)) {
            st = mid;
        } else {
            en = mid - 1;
        }
    }
    cout << st;
}