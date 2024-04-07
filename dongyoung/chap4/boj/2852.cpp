/**
 * BOJ 2852 NBA 농구
 * 골이 들어간 시간, 팀
 * 농구경기 48분
 * 각 팀이 몇분동안 이기고 있었는지 출력
 *
 * 골이 들어간 횟수 N
 *
 * 득점 정보 n줄에 받기
 *
 * 득점한 팀의 번호, 득점한 시간
 * 팀 번호는 1, 2
 * 시간은 MM:SS
 * 한자리면 0
 * 0 <= M <= 47
 * 0 <= S <= 59
 *
 * 득점시간 겹치는 거 x
 *
 * 1 team MM:SS
 * 2 team MM:SS
 */
#include <bits/stdc++.h>
using namespace std;

int winningTime[3];
int score[3];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, teamNum;
    int state = 0;
    string timeInput;
    cin >> n;
    int prevSecond = 0;
    for (int i = 0; i < n; ++i) {
        cin >> teamNum >> timeInput;
        int inputSecond =
                ((timeInput[0] - '0') * 10 + (timeInput[1] - '0')) * 60 + (timeInput[3] - '0') * 10 + timeInput[4] -
                '0'; // 입력 받은 시간을 초로 다 환산
        int prevState = state;
        score[teamNum]++;
        if(score[1] > score[2]) {
            state = 1;
        }
        if (score[2] > score[1]) {
            state = 2;
        }
        if (score[1] == score[2]) {
            state = 0;
        }

        if (state != prevState) {
            winningTime[prevState] += inputSecond - prevSecond;
            prevSecond = inputSecond;
        }
    }

    winningTime[state] += 48 * 60 - prevSecond;

    string min, sec;
    if (winningTime[1] / 60 < 10) {
        min = '0' + to_string(winningTime[1] / 60);
    } else {
        min = to_string(winningTime[1] / 60);
    }
    if (winningTime[1] % 60 < 10) {
        sec = '0' + to_string(winningTime[1] % 60);
    } else {
        sec = to_string(winningTime[1] % 60);
    }
    cout << min << ':' << sec << '\n';
    if (winningTime[2] / 60 < 10) {
        min = '0' + to_string(winningTime[2] / 60);
    } else {
        min = to_string(winningTime[2] / 60);
    }
    if (winningTime[2] % 60 < 10) {
        sec = '0' + to_string(winningTime[2] % 60);
    } else {
        sec = to_string(winningTime[2] % 60);
    }
    cout << min << ':' << sec << '\n';


}