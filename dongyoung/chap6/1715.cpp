/**
 * BOJ 1715 카드 정렬하기 골드 4
 *
 * 정렬된 카드 합칠 때 최소한의 비교하도록
 *
 * 입력:
 * N(1 < N <= 100000)
 * N 줄 카드 묶음 크기(1000 이하의 양의 정수)
 *
 * 출력:
 * 최소 비교 횟수
*/

#include <bits/stdc++.h>
using namespace std;
int n;
vector<int> card;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    int input;
    for (int i = 0; i < n; i++) {
        cin >> input;
        card.push_back(input);
    }
    priority_queue<int, vector<int>, greater<int> >
            minQueue(card.begin(), card.end());

    int a, b, ans = 0;
    while (true) {
        a = minQueue.top();
        minQueue.pop();
        if (minQueue.empty()) {
            break;
        }
        b = minQueue.top();
        minQueue.pop();
        minQueue.push(a + b);
        ans += (a + b);
    }
    cout << ans;



}