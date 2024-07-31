#include <bits/stdc++.h>
using namespace std;

int alpha[26];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    string s;
    cin >> s;
    for (auto letter: s) {
        if(letter - 'a' >= 0) {
            alpha[letter - 'a']++;
        } else {
            alpha[letter - 'A']++;
        }
    }
    int max = -1;
    int idx = -1;
    for (int i = 0; i < 26; i++) {
        if (alpha[i] == 0) {
            continue;
        }
        if (alpha[i] > max) {
            max = alpha[i];
            idx = i;
        } else if (alpha[i] == max) {
            idx = -1;
        }
    }

    if (idx == -1) {
        cout  << '?';
    } else {
        cout << char(idx + 'A');
    }

}