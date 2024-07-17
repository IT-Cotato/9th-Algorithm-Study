#include <bits/stdc++.h>

using namespace std;

int n;
int num[100001], d[100001];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> num[i];
    }

    d[0] = num[0];
    for (int i = 1; i < n; i++) {
        d[i] = max(d[i - 1] + num[i], num[i]);
    }
    cout << *max_element(d, d + n);

}
