#include <bits/stdc++.h>
using namespace std;

int arr[1005];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, m, k;
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n); // 배열 오름차순 정렬

    int x = arr[n-1]; // 가장 큰 값
    int y = arr[n-2]; // 두번째 큰 값

    int r = m % (k + 1); // 나머지
    int d = m / (k + 1); // 몫

    // k+1 로 나누어 떨어질 때와 아닐 때로 나누어 계산
    if (r == 0) {
        cout << (k * x + y) * d;
    } else {
        cout << (k * x + y) * d + r * x;
    }

}