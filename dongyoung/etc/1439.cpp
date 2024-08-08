#include<bits/stdc++.h>
using namespace std;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;
    int cnt0 = 0, cnt1 = 0;

    bool prev;

    if (s[0] == '0') {
        prev = 0;
        cnt0++;
    } else {
        prev = 1;
        cnt1++;
    }
    for (int i = 1; i < s.size(); i++) {
        if(prev && s[i] == '0') { // 1 -> 0
            cnt0++;
            prev = 0;
        } else if(!prev && s[i] == '1'){ // 0 -> 1
            cnt1++;
            prev = 1;
        }
    }

    cout << min(cnt0, cnt1);

}