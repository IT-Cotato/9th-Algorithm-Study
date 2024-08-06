#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> frd[501];
bool invited[501];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        frd[a].push_back(b);
        frd[b].push_back(a);
    }

    // 1과 친구인 사람 모음
    for (auto f: frd[1]) {
        // 1의 친구의 친구
        invited[f] = true;
        for (auto ff: frd[f]) {
            invited[ff] = true;
        }
    }

    int result = -1;

    for (auto i: invited) {
        if(i) {
            result++;
        }
    }
    if (result == -1) {
        cout << 0;
    } else {
        cout << result;
    }


}