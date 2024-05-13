/**
 * BOJ 10816 숫자카드 2
 * N개의 숫자
 */

#include <bits/stdc++.h>
using namespace std;
int n, m;
vector<int> v;
vector<int> arr;

int bSearch(iterator<Vector<int> > begin, iterator<Vector<int> > end, int i) {
    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    int inputArr;
    for (int i = 0; i < n; i++) {
        cin >> inputArr;
        arr.push_back(inputArr);
    }
    sort(arr, arr + n);
    cin >> m;
    int input;
    for (int i = 0; i < m; i++) {
        cin >> input;
        v.push_back(input);
    }
    for (int i: v) {
        int cnt = 0;
        if (binary_search(arr.begin(), arr.end(), i)) {
            cnt++;
        }
    }
}