/**
 * BOJ 11404 플로이드 골드4
 * n개의 도시
 * m개의 버스
 *
 */

#include <bits/stdc++.h>
using namespace std;

const int INF = 0x3f3f3f3f;
int n, m;
int board[102][102];

int main() {

    ios::sync_with_stdio(0);
    cin.tie(0);


    cin >> n >> m;
    for(int i = 1; i <= n; i++) {
        fill(board[i], board[i] + n + 1, INF);
    }
    for (int i = 0; i < m; i++) {
        int st, en, cost;
        cin >> st >> en >> cost;
        board[st][en] = min(cost, board[st][en]);
    }

    for (int i = 1; i <= n; i++) {
        board[i][i] = 0;
    }

    for(int k = 1; k <= n; k++) {
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                board[i][j] = min(board[i][j], board[i][k] + board[k][j]);
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if(board[i][j] == INF) {
                cout << 0 << ' ';
            } else {
                cout << board[i][j] << ' ';
            }
        }
        cout << '\n';
    }

}