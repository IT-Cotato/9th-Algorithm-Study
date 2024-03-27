#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int n, k;
    cin >> n >> k;
    int cnt = 0;
    while(n != 1) {
        if (n % k != 0) {
            n--;
            cnt++;
        } else {
            n /= k;
            cnt++;
        }
    }
    cout << cnt;
}