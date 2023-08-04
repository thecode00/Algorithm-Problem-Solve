// https://school.programmers.co.kr/learn/courses/30/lessons/17680

#include <string>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

int solution(int cacheSize, vector<string> cities)
{
    int time = 0;
    deque<string> cache;

    for (auto city : cities)
    {
        transform(city.begin(), city.end(), city.begin(), ::tolower); // city를 소문자로 만듬
        // city가 캐시에 존재하는지 검사
        auto it = find(cache.begin(), cache.end(), city);
        if (it == cache.end())
        {
            time += 5;
        }
        else
        {
            time += 1;
            cache.erase(find(cache.begin(), cache.end(), city));
        }
        cache.emplace_back(city);
        // 캐시가 가득찬경우 제일먼저 들어온 city를 삭제
        if (cache.size() > cacheSize)
        {
            cache.pop_front();
        }
    }

    return time;
}