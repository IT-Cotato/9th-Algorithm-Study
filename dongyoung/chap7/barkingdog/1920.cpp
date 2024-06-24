#include <bits/stdc++.h>
using namespace std;
int arr[100002];
int n, m;

int binarySearch(int target) {
    int st = 0;
    int en = n - 1;
    while (st <= en) {
        int mid = (st + en) / 2;
        if (arr[mid] == target) {
            return 1;
        } else if (target < arr[mid]) {
            en = mid - 1;
        } else {
            st = mid + 1;
        }
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    sort(arr, arr + n);
    vector<int> v;
    cin >> m;
    int input;
    for (int i = 0; i < m; i++) {
        cin >> input;
        cout << binarySearch(input) << '\n';
    }

}