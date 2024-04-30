/**
 * BOJ 10825 국영수 실버4
 * 국어 점수가 감소하는 순서
 * 국어점수 같으면 영어점수 증가하는 순서
 * 국, 영 같으면 수학 감소하는 순서
 * 모든 점수가 같으면 사전순 증가하는 순서(대문자가 소문자보다 앞에)
 * 학생수 N 주어짐
 * 한줄에 하나씩 이름, 국, 영, 수 입력
 * 학생 이름 순서대로 출력
 */

#include <bits/stdc++.h>
using namespace std;
int n;

struct Student {
    string name;
    int kor, eng, mth;
};

bool cmp(Student &s1, Student &s2) {
    if (s1.kor != s2.kor) {
        return s1.kor > s2.kor;
    } else if (s1.eng != s2.eng) {
        return s1.eng < s2.eng;
    } else if (s1.mth != s2.mth) {
        return s1.mth > s2.mth;
    } else {
        return s1.name < s2.name;
    }
}
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n;
    struct Student student[n];
    for (int i = 0; i < n; ++i) {
        cin >> student[i].name >> student[i].kor >> student[i].eng >> student[i].mth;
    }

    sort(student, student + n, cmp);
    for (int i = 0; i < n; ++i) {
        cout << student[i].name << '\n';
    }
}