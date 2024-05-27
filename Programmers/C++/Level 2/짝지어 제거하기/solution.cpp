// https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=cpp

#include <string>
#include <vector>

using namespace std;

int solution(string s)
{
    vector<char> stack;

    for (auto c : s)
    {
        // 제거할수있는 알파벳 짝이 있다면 바로바로 제거
        if (stack.size() > 0 && stack.back() == c)
        {
            stack.pop_back();
        }
        else
        {
            stack.emplace_back(c);
        }
    }

    return stack.size() > 0 ? 0 : 1;
}