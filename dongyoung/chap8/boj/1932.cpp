/**
* BOJ 1932 정수 삼각형 실버1
 * 입력: n(1 ~ 500), 정수 삼각형
 * 출력: 합이 최대가 되는 경로에 있는 수의 합
*/
#include <bits/stdc++.h>
using namespace std;

int n;
int input[501][501];
int d[501][501];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cin >> input[i][j];
        }
    }
    d[1][1] = input[1][1];
    d[2][1] = input[1][1] + input[2][1];
    d[2][2] = input[1][1] + input[2][2];
    for (int i = 3; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            d[i][j] = max(d[i-1][j-1], d[i-1][j]) + input[i][j];
        }
    }
    int mx = d[n][1];
    for (int i = 1; i <= n; i++) {
        mx = max(mx, d[n][i]);
    }
    cout << mx;

}