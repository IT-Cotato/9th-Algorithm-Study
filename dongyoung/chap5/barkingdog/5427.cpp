/**
 * BOJ 5427 불 골드4
 * 불이 매초 동서남북 빈 공간으로 퍼져나간다.
 * 상근이 이동 동서남북 한 칸, 1초
 * 벽 통과 불가
 * 불이 붙으려는 칸, 불이 붙은 칸 이동 불가
 * 상근이 있는 칸에 불이 옮겨옴과 동시에 이동 가능
 * 빌딩의 지도 주어졌을 때 얼마나 빨리 탈출할 수 있을지
 * 테스트 케이스 개수 t <= 100
 * 빌딩 w, h(1 <= w, h <= 1000)
 * . : 빈 공간
 * # : 벽
 * @ : 상근이 시작 위치
 * * : 불
 * 탈출 가능시 가장 빠른 시간 출력
 * 불가능시 "IMPOSSIBLE" 출력
 *
 * 상근이가 출구로 나가는 경로를 파악
 * 불도 출구로 가는 경로 파악

 */
#include <bits/stdc++.h>
#define X first
#define Y second
using namespace std;


int t, w, h;
char building[1002][1002];
queue<pair<int, int> > sg;
queue<pair<int, int> > fire;
int dx[4] = {1, 0, -1, 0};
int dy[4] = {0, 1, 0, -1};

void resetBuilding() {
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            building[i][j] = '.';
        }
    }
    while (!sg.empty()) {
        sg.pop();
    }
    while (!fire.empty()) {
        fire.pop();
    }
}

void moveFire() {
    int cnt = fire.size();
    for (int i = 0; i < cnt; i++) {
        pair<int, int> cur = fire.front();
        fire.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.X + dx[dir];
            int ny = cur.Y + dy[dir];
            if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
                continue;
            }
            if (building[nx][ny] != '.') {
                continue;
            }
//            if(building[nx][ny] == '#') continue;
            building[nx][ny] = '*';
            fire.push(make_pair(nx, ny));
        }
    }
}

int moveSg() {
    int time = 0;
    while (!sg.empty()) {
        time++;
        moveFire();
        int cnt = sg.size();
        for (int i = 0; i < cnt; i++) {
            pair<int, int> cur = sg.front();
            sg.pop();
            for (int dir = 0; dir < 4; dir++) {
                int nx = cur.X + dx[dir];
                int ny = cur.Y + dy[dir];
                if (nx < 0 || nx >= h || ny < 0 || ny >= w) {
                    return time;
                }
                if ( building[nx][ny] != '.') {
                    continue;
                }
                sg.push(make_pair(nx, ny));
                building[nx][ny] = '@';
            }
        }
    }
    return -1;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> t;
    for (int iter = 0; iter < t; iter++) {
        cin >> w >> h;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                cin >> building[i][j];
                if(building[i][j] == '*') {
                    fire.push(make_pair(i, j));
                } else if (building[i][j] == '@') {
                    sg.push(make_pair(i, j));
                }
            }
        }
        int count = moveSg();
        if (count == -1) {
            cout << "IMPOSSIBLE" << '\n';
        } else {
            cout << count << '\n';
        }
        resetBuilding();
    }
}