/**
 * BOJ 18310 안테나 실버 3
 * 안테나로 부터 모든 집까지 거리의 총 합이 최소인 안테나의 위치 구하기
 * 집의 수 N
 * 둘 째 줄에 N채의 집의 위치 주어짐
 *
 * 안테나를 설치할 위치의 값 출력
 * 여러 값일 경우 가장 작은 값 출력
 */

#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;
int n;
int house[200002];
int ans; // 답 저장용

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> house[i];
    }
    sort(house, house + n);
    if (n % 2 == 0) { // 짝수
        ans = house[n / 2 - 1];
    } else {
        ans = house[n / 2];
    }
    cout << ans;
}