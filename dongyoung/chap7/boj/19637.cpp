#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<pair<string, int> > tier;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        string s;
        int power;
        cin >> s >> power;
        tier.push_back(make_pair(s, power));
    }

    for (int i = 0; i < m; i++) {
        int p;
        cin >> p;
        int st, en;
        st = 0;
        en = n-1;
        int result = 0;
        while (st <= en) {
            int mid = (st + en) / 2;
            if (p <= tier[mid].second) {
                result = mid;
                en = mid - 1;
            } else {
                st = mid + 1;
            }
        }

        cout << tier[result].first << '\n';


    }

}