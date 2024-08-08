#include<bits/stdc++.h>
using namespace std;

int n;
unsigned long long d[101][101];
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    d[0][1] = 1;
    d[0][10] = 0;
    for (int i = 1; i <= 9; i++) {
        d[i][1] = 1;
    }

    if(n == 1) {
        unsigned long long result = 0;
        for (int i = 1; i <= 9; i++) {
            result = (result + d[i][1]) % 1000000000;
        }
        cout << result;
        return 0;
    }

    for (int level = 2; level <= n; level++) {
        for (int i = 0; i <= 9; i++) {
            if(i == 0) {
                d[i][level] = d[i+1][level-1];
            } else if(i == 9){
                d[i][level] = d[i-1][level-1];
            } else {
                d[i][level] = (d[i-1][level-1] % 1000000000) + (d[i+1][level-1] % 1000000000);
            }
        }
    }
    unsigned long long result = 0;
    for (int i = 1; i <= 9; i++) {
        result = (result + d[i][n] % 1000000000) % 1000000000;
    }
    cout << result;

}