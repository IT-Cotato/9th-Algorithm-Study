#include <bits/stdc++.h>
#define MAX 0x7f7f7f7f
using namespace std;

int n, d; // 지름길의 개수, 고속도로의 길이

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> d;

    vector<int> map(d+1, MAX);
    vector<pair<int, int>> to[10001]; // {출발 지점 , 길이}

    for(int i = 0; i < n; i++) {
        int st, en, distance;
        cin >> st >> en >> distance;
        to[en].push_back({st, distance});
    }

    map[0] = 0;
    for (int i = 1; i <= d; i++) {
        if (to[i].size() == 0) {
            map[i] = map[i-1] + 1;
        } else {
            for (auto v: to[i]) {
                map[i] = min(map[i], min(map[i-1] + 1, map[v.first] + v.second));
            }
        }
    }

    cout << map[d] << '\n';



}