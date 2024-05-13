/**
 * BOJ 20006 랭킹전 대기열 실버 1
 *
 * 매칭 가능한 방 x
 *  새로운 방 생성
 *  방장 레벨 -10 ~ 10 가능
 *
 * 매칭 가능
 *  입장시키고 정원 찰때까지 대기
 *  먼저 생성된 방 먼저 참
 *
 *  플레이어의 수 p, 플레이어의 닉네임 n, 플레이어의 레벨 l, 방 한개의 정원 m
 *  만들어진 방의 상태와 입장 플레이어들을 출력
 */

#include <bits/stdc++.h>
using namespace std;
int p, m, l[305];
string n[305];

bool cmp(const pair<int, string> &a, const pair<int, string> &b) {
    if(a.second < b.second) {
        return true;
    } else {
        return false;
    }
}
struct Room {
    int lowLimit, highLimit, member;
    vector<pair<int, string> > members;
};
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin >> p >> m;
    for (int i = 0; i < p; ++i) {
        cin >> l[i] >> n[i];
    }
    vector<Room> rooms;
    Room r;
    if (l[0] <= 10) {
        r.lowLimit = 1;
        r.highLimit = l[0] + 10;
    } else if (l[0] > 490) {
        r.lowLimit = l[0] - 10;
        r.highLimit = 500;
    } else {
        r.lowLimit = l[0] - 10;
        r.highLimit = l[0] + 10;
    }
    r.member = 1;
    r.members.push_back(make_pair(l[0], n[0]));

    rooms.push_back(r);

    bool isEntered = false;

    for (int i = 1; i < p; i++) {
        isEntered = false;
        for (auto &j: rooms) {
            if (j.member < m && l[i] >= j.lowLimit && l[i] <= j.highLimit) {
                j.members.push_back(make_pair(l[i], n[i]));
                j.member++;
                isEntered = true;
                break;
            }
        }
        if (!isEntered) {
            //새 방을 만들자
            Room newRoom;
            if (l[i] <= 10) {
                newRoom.lowLimit = 1;
                newRoom.highLimit = l[i] + 10;
            } else if (l[i] > 490) {
                newRoom.lowLimit = l[i] - 10;
                newRoom.highLimit = 500;
            } else {
                newRoom.lowLimit = l[i] - 10;
                newRoom.highLimit = l[i] + 10;
            }
            newRoom.member = 1;
            newRoom.members.push_back(make_pair(l[i], n[i]));
            rooms.push_back(newRoom);
        }
    }

    for (auto &roomIter: rooms) {
        sort(roomIter.members.begin(), roomIter.members.end(), cmp);
        if (roomIter.member == m) {
            cout << "Started!" << '\n';
            for (int i = 0; i < m; i++) {
                cout << roomIter.members[i].first << ' ' << roomIter.members[i].second << '\n';
            }
        } else {
            cout << "Waiting!" << '\n';
            for (int i = 0; i < roomIter.member; i++) {
                cout << roomIter.members[i].first << ' ' << roomIter.members[i].second << '\n';
            }
        }
    }
}