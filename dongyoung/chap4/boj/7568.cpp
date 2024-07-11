#include <bits/stdc++.h>
using namespace std;

int n;
int ans[51];
vector<pair<int, int> > person;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;

    for (int i = 0; i < n; i++) {
        int w, h;
        cin >> w >> h;
        person.push_back(make_pair(w, h));
    }


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                continue;
            }
            if (person[i].first < person[j].first && person[i].second < person[j].second) {
                ans[i]++;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        cout << ans[i] + 1 << ' ';
    }


}