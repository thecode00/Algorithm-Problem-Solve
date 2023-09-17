// https://school.programmers.co.kr/learn/courses/30/lessons/12938?language=cpp

#include <algorithm>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, int s)
{
    vector<int> answer;
    if (n > s)
    {
        answer.emplace_back(-1);
        return answer;
    }
    int q = s / n, r = s % n;
    for (int i = 0; i < n; i++)
    {
        answer.emplace_back(q);
        if (r > 0)
        {
            answer.back() += 1;
            r -= 1;
        }
    }
    reverse(answer.begin(), answer.end());
    return answer;
}