/**
* BOJ 2343 기타 레슨 실버 1
 * m개의 블루레이에 모든 기타 강의 녹화해야 함
 * 강의의 수 N(1 <= N <= 100,000), M(1 <= M <= N)
 * 강토의 강의 길이 순서대로 분 단위 자연수로 주어짐(최대 10000분)
 * 가능한 블루레이 크기 중 최소 출력
 *
 * m개의 블루레이에 n개의 강의를 담을 수 있는 블루레이의 크기의 최소값 구하기
 * -> 블루레이의 크기가 x 일 때, m개의 블루레이에 n개의 강의를 담을 수 있는가?
*/

#include <bits/stdc++.h>
using namespace std;
int n, m;
int lecture[100002];

int solve(int amount) {
    int sum = 0;
    int cnt = 1;
    for (int i = 0; i < n; i++) {
        sum += lecture[i];
        if (sum + lecture[i+1] > amount) {
            sum = 0;
            cnt++;
        }
    }
    return cnt;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int result;
    int st = -1;
    int en = 0;

    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        cin >> lecture[i];
        en += lecture[i];
        st = max(lecture[i], st);
    }

    while(st <= en) {
        int mid = (st + en) / 2;
        if (solve(mid) <= m) {
            en = mid - 1;
            result = mid;
        } else {
            st = mid + 1;
        }
    }
    cout << result;
}