/**
* BOJ 14888 연산자 끼워넣기 실버 1
 * n개의 수열 주어짐
 * A1 ... An
 * 연산자 n-1개 주어짐
 * + - * /
 * 6 수열 5연산자(+ + - * / ) -> 60가지(5! / 2)
 * 앞에서 부터 진행
 * 나눗셈: 음수일 때는 양수로 바꾼 후 몫을 취하고 음수로 바꾼 것
 * 결과 : 만들 수 있는 식의 결과 최대, 최소
 *
*/

#include <bits/stdc++.h>
using namespace std;

int n, result;
int arr[12];
int op[4]; // + - * /

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    for (int & i : op) {
        cin >> i;
    }
    string s;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < op[i]; j++) {
            s.push_back(i + '0');
        }
    }
    int mx = -1000000001;
    int mn = 1000000001;
    do {
        result = arr[0];
        for (int i = 0; i < n-1; i++) {
            if(s[i] == '0') {
                result += arr[i + 1];
            } else if (s[i] == '1') {
                result -= arr[i + 1];
            } else if (s[i] == '2') {
                result *= arr[i + 1];
            } else {
                result /= arr[i + 1];
            }
        }
        mx = max(mx, result);
        mn = min(mn, result);
    } while (next_permutation(s.begin(), s.end()));

    result = arr[0];
    for (int i = 0; i < n-1; i++) {
        if(s[i] == '0') {
            result += arr[i + 1];
        } else if (s[i] == '1') {
            result -= arr[i + 1];
        } else if (s[i] == '2') {
            result *= arr[i + 1];
        } else {
            result /= arr[i + 1];
        }
    }
    mx = max(mx, result);
    mn = min(mn, result);

    cout << mx << '\n' << mn;

}