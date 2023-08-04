// https://school.programmers.co.kr/learn/courses/30/lessons/17682?language=cpp

#include <string>
#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

int solution(string dartResult)
{
    vector<int> scores;
    scores.emplace_back(0);

    for (auto result : dartResult)
    {
        if (result == 'S')
        {
            scores.emplace_back(0);
        }
        else if (result == 'D')
        {
            scores.back() = pow(scores.back(), 2);
            scores.emplace_back(0);
        }
        else if (result == 'T')
        {
            scores.back() = pow(scores.back(), 3);
            scores.emplace_back(0);
        }
        else if (result == '*')
        {
            // 이전점수와 그 이전점수를 다 2배로 함
            scores[scores.size() - 2] *= 2;
            if (scores.size() > 2)
            {
                scores[scores.size() - 3] *= 2;
            }
        }
        else if (result == '#')
        {
            scores[scores.size() - 2] *= -1;
        }
        else
        {
            // char형은 아스키코드가 정수형으로 저장되어있어서 int형으로 형변환을 할경우 '1'이 1이아닌 1을 표현하는 아스키코드인 49로 바뀐다
            // 그러므로 정수형으로 변환한다음 0의 아스키코드인 48을 빼야한다
            scores.back() = scores.back() * 10 + (int(result) - 48);
        }
    }
    int total = 0;
    for (auto score : scores)
    {
        total += score;
    }
    return total;
}