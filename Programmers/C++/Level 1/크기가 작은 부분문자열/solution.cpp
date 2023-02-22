// https://school.programmers.co.kr/learn/courses/30/lessons/147355?language=cpp#


#include <string>
#include <vector>

using namespace std;

int solution(string t, string p) {
    int count = 0;
    int left = 0;
    for (int i = 0; i <= t.size() - p.size(); i++){
        int right = i + p.size();
        if (stol(t.substr(i, p.size())) <= stol(p)){
            count += 1;
        }
    }
    return count;
}