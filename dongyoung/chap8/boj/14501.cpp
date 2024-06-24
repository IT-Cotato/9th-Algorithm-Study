/**
* BOJ 14501 퇴사 실버3
 * 입력: n(1 ~ 15), Ti(상담 완료까지 걸리는 기간), Pi(얻을 수 있는 금액)
 * 출력: 얻을 수 있는 최대 이익
*/

#include <bits/stdc++.h>
using namespace std;

int n;
int t[16];
int p[16];
int d[16]; // i번째 날에 일이 끝날 때 최대 이익


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; ++i) {
        cin >> t[i] >> p[i];
    }

    for (int i = 1; i <= n; i++) {
        d[i] = max(d[i], d[i - 1]);

        if(i + t[i] <= n + 1) {
            d[i + t[i] - 1] = max(d[i-1] + p[i], d[i + t[i] - 1]);
        }
    }
    cout << *max_element(d + 1, d + n + 1);

}