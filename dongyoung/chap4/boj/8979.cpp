/**
* 백준 8979 올림픽
 * 국가 : 1 ~ N 사이 정수
 *
*/

#include <bits/stdc++.h>
using namespace std;

struct medal {
    int id, gold, silver, bronze;

    bool operator >(const medal &m) const {
        if (gold != m.gold) {
            return gold > m.gold;
        } else if (silver != m.silver) {
            return silver > m.silver;
        } else {
            return bronze > m.bronze;
        }
    }
};


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;

    vector<medal> v(n);

    for (int i = 0; i < n; i++) {
        cin >> v[i].id >> v[i].gold >> v[i].silver >> v[i].bronze;
    }

    sort(v.begin(), v.end(), greater<medal>());

    int rank = 1, same = 0;

    for (int i = 0; i < n; i++) {
        if (i > 0 &&
        v[i].gold != v[i-1].gold ||
        v[i].silver != v[i-1].silver ||
        v[i].bronze != v[i-1].bronze) {
            rank += same;
            same = 0;
        }
        if (v[i].id == k) {
            cout << rank;
            return 0;
        }
        same++;

    }



}