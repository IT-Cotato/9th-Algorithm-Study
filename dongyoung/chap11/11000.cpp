/**
 * BOJ 11000 강의실 배정 골드 5
 * 정수 n을 입력받아서
 * Si, Ti를 받아서
 * 강의실의 개수 출력
 *
 * Ti <= Sj인 경우 i, j를 같이 들을 수 있다.
 * 강의 시작시간 s, 강의 끝나는 시간 t
 */
#include <bits/stdc++.h>
using namespace std;
int n;
vector<pair<int, int> > lectures;
priority_queue<int, vector<int>, greater<int> > pq;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> n;
    for (int i = 0; i < n; i++) {
        int s, t;
        cin >> s >> t;
        lectures.push_back(make_pair(s, t));
    }

    sort(lectures.begin(), lectures.end());

    pq.push(lectures[0].second); // 첫 번째 강의 끝나는 시간 추가
    for (int i = 1; i < lectures.size(); i++) {
        if (pq.top() <= lectures[i].first) {
            pq.pop();
            pq.push(lectures[i].second);
        } else {
            pq.push(lectures[i].second);
        }
    }

    cout << pq.size();

}