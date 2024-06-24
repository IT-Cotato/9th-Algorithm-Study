#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<int> v[105];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int tmp;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> tmp;
            v[i].push_back(tmp);
        }
        sort(v[i].begin(), v[i].end());
    }
    int mx = -1;
    for (int i = 0; i < n - 1; i++) {
       mx = max(v[i].front(), v[i + 1].front());
    }
    cout << mx;
}