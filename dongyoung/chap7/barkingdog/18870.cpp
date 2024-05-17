/**
* BOJ 18870 좌표 압축 실버2
 * 좌표 x1 ~ xn
 * 좌표 압축한 xi' = xi > xj 인 xj의 개수
 * (자기보다 작은 값의 개수)
 *
*/

#include <bits/stdc++.h>
using namespace std;

int n;
int arr[1000002];
vector<int> tmp, uni;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
        tmp.push_back(arr[i]);
    }
    sort(tmp.begin(), tmp.end());
    for (int i = 0; i < n; i++) {
        if (i == 0 || tmp[i - 1] != tmp[i]) {
            uni.push_back(tmp[i]);
        }
    }
    for (int i = 0; i < n; i++) {
        cout << lower_bound(uni.begin(), uni.end(), arr[i]) - uni.begin() << ' ';
    }

}