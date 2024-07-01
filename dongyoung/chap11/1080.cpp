#include<bits/stdc++.h>
using namespace std;

int n, m;
int matA[51][51], matB[51][51];
bool arr[51][51];

void change(int ii, int jj) {
    for (int i = ii; i < ii + 3; i++) {
        for (int j = jj; j < jj + 3; j++) {
            if (matA[i][j] == 1) {
                matA[i][j] = 0;
            } else {
                matA[i][j] = 1;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            matA[i][j] = s[j] - '0';
        }
    }
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            matB[i][j] = s[j] - '0';
        }
    }

    int cnt = 0;

    for (int i = 0; i < n - 2; i++) {
        for (int j = 0; j < m - 2; j++) {
            if (matA[i][j] != matB[i][j]) {
                change(i, j);
                cnt++;
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (matA[i][j] != matB[i][j]) {
                cout << -1;
                return 0;
            }
        }
    }
    cout << cnt;
    return 0;

}