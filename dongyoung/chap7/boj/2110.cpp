/**
* BOJ 2110 공유기 설치 골드4
 * 집 n개가 수직선 위에
 * 와이파이 공유기 C개 설치
*/

#include <bits/stdc++.h>
using namespace std;
int n, c;
vector<int> house;

bool solve(int dist) {
    for (int i = 0; i < house.size(); i++) {
        for (int j = i+1; j < house.size(); j++) {
            if (i == j) {
                continue;
            }
            if (house[i] + dist < house[j]) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int st = 1, en = -1, tmp;
    cin >> n >> c;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        house.push_back(tmp);
        en = max(tmp, en);
    }
    while(st < en) {
        int mid = (st + en) / 2;
        if(solve(mid)) {
            st = mid;
        } else {
            en = mid - 1;
        }
    }
    cout << st;

}