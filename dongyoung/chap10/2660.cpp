#include <bits/stdc++.h>
#define MAX 0x3f3f3f3f
using namespace std;

int n;
int arr[51][51];
vector<int> ans;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    for(auto i : arr) {
        fill(i, i + 51, MAX);
    }
    for (int i = 0; i < 51; i++) {
        arr[i][i] = 0;
    }

    cin >> n;

    while(true) {
        int a, b;
        cin >> a >> b;
        if (a == -1 && b == -1) {
            break;
        }
        arr[a][b] = 1;
        arr[b][a] = 1;
    }

    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                arr[i][j] = min(arr[i][k] + arr[k][j], arr[i][j]);
            }
        }
    }

    int cnt = 0;
    int minMax = MAX;
    for (int i = 1; i <= n; i++) {
        int mx = -1;
        for (int j = 1; j <= n; j++) {
            mx = max(mx, arr[i][j]);
        }
        if(mx < minMax) {
            cnt = 1;
            ans.clear();
            ans.push_back(i);
            minMax = mx;
        } else if(mx == minMax) {
            ans.push_back(i);
            cnt++;
        }
    }

    cout << minMax << ' ' << cnt << '\n';
    for(auto p : ans) {
        cout << p << ' ';
    }


}