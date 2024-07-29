#include <bits/stdc++.h>

using namespace std;

int n;
long long d[31][31];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    while(true) {
        cin >> n;
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            cout << 1 << '\n';
            continue;
        }
        if (n == 2) {
            cout << 2 << '\n';
            continue;
        }


        for (int i = 0; i < n; i++) {
            fill(d[i], d[i] + n, 0);
        }

        for (int i = 0; i <= n; i++) {
            d[n-i][i] = 1;
        }
        int index = n-1;
        while (index > 0) {
            d[index][0] = d[index][1];
            for (int i = index - 1; i >= 0; i--) {
                d[i][index-i] = d[i][index-i+1] + d[i+1][index-i-1];
            }
            index--;
        }
        d[0][0] = d[1][0] + d[0][2];

        cout << d[0][0] << '\n';
    }


}