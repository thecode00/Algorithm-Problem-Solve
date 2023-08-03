// https://school.programmers.co.kr/learn/courses/30/lessons/17678

#include <string>
#include <deque>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;

string solution(int n, int t, int m, vector<string> timetable)
{
    deque<int> minuteTable;
    // 시간을 분으로 변환
    for (auto time : timetable)
    {
        // 시간 * 60 + 분
        minuteTable.emplace_back(stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3, 5)));
    }
    sort(minuteTable.begin(), minuteTable.end());
    int currentTime = 540; // 9:00시, 셔틀버스가 맨 처음 오는 시간
    int conTime;           // 콘이 줄서는 시간

    for (int i = 0; i < n; i++) // 셔틀버스 운행 횟수
    {
        for (int j = 0; j < m; j++) // 셔틀버스 크루수
        {
            // 대기하는 사람이있으면 맨 마지막에 대기하는 사람보다 1분 일찍옴
            if (!minuteTable.empty() && minuteTable.front() <= currentTime)
            {
                conTime = minuteTable.front() - 1;
                minuteTable.pop_front();
            }
            else // 대기하는 사람이 없으면 셔틀버스시간에 맞춰옴
            {
                conTime = currentTime;
            }
        }
        currentTime += t; // 다음 셔틀버스
    }

    stringstream ss;
    // setfill은 한번만 설정해도 자동으로 뒤의 문자들에 적용이됨
    ss << setw(2) << setfill('0') << conTime / 60 << ':' << setw(2) << conTime % 60;
    return ss.str();
}