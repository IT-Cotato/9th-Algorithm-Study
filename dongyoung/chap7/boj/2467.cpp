#include <bits/stdc++.h>

using namespace std;
int n;
int liq[100001];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> liq[i];
    }
    int value, mn = 2100000000;
    int idA = -1, idB = -1;

    int st = 0, en = n-1;
    while (st < en) {
        int sum = liq[st] + liq[en];
        if (abs(sum) < abs(mn)) {
            idA = st;
            idB = en;
            mn = sum;
        }

        if (sum < 0) {
            st ++;
        } else if (sum > 0) {
            en--;
        } else {
            break;
        }
    }

    cout << liq[idA] << ' ' << liq[idB];


}