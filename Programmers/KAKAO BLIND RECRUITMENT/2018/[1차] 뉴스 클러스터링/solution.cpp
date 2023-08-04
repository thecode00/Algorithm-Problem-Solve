// https://school.programmers.co.kr/learn/courses/30/lessons/17677?language=cpp

#include <string>
#include <regex>
#include <vector>
#include <iostream>
#include <algorithm>
#include <set>

using namespace std;

void split(multiset<string> &titleSet, string &title)
{
    regex word("[a-z]{2}"); // 정규식으로 영단어 2글자만 고름
    string subTitle;
    for (int idx = 0; idx < title.size() - 1; idx++)
    {
        subTitle = title.substr(idx, 2);
        transform(subTitle.begin(), subTitle.end(), subTitle.begin(), ::tolower); // 대소문자 구분을 안하므로 다 소문자로 만듬
        if (regex_match(subTitle, word))                                          // 자른 2글자가 영어로만 이루어져있을경우에만 추가
        {
            titleSet.insert(subTitle);
        }
    }
}

int solution(string str1, string str2)
{
    multiset<string> setStr1, setStr2;
    split(setStr1, str1);
    split(setStr2, str2);
    // 교집합 합집합만들기
    multiset<string> intersection, setUnion;
    set_intersection(setStr1.begin(), setStr1.end(), setStr2.begin(), setStr2.end(), inserter(intersection, intersection.begin()));
    set_union(setStr1.begin(), setStr1.end(), setStr2.begin(), setStr2.end(), inserter(setUnion, setUnion.begin()));
    // 테스트 코드
    // for (auto s : intersection)
    // {
    //     cout << s << endl;
    // }
    // cout << "-----" << endl;
    // for (auto s : setUnion)
    // {
    //     cout << s << endl;
    // }

    // Divide by zero방지
    return setUnion.size() == 0 ? 65536 : (float)intersection.size() / setUnion.size() * 65536;
}