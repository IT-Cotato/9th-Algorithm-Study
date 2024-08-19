#include <bits/stdc++.h>
using namespace std;

int n, m;
long long result = 0;
priority_queue<long long, vector<long long>, greater<long long> >  pq;

void solution() {
    long long a = pq.top();
    pq.pop();
    long long b = pq.top();
    pq.pop();

    pq.push(a + b);
    pq.push(a + b);
}

void sum() {
    while(!pq.empty()) {
        result += pq.top();
        pq.pop();
    }
}

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        long long num;
        cin >> num;
        pq.push(num);
    }

    for (int i = 0; i < m; i++) {
        solution();
    }
    sum();

    cout << result;

}