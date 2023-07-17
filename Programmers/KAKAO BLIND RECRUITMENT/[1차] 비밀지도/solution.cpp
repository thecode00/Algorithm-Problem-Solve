// https://school.programmers.co.kr/learn/courses/30/lessons/17681?language=cpp

#include <string>
#include <vector>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2)
{
    vector<string> answer;
    for (int idx = 0; idx < n; idx++)
    {
        string row = "";
        int grid = arr1[idx] | arr2[idx];
        // row.size() < n가 아닌 grid > 0을 해버리면 row의 길이가 n이되기전에 루프가 끝날수도있음
        while (row.size() < n)
        {
            grid % 2 == 1 ? row = "#" + row : row = " " + row;
            grid >>= 1;
        }
        answer.push_back(row);
    }
    return answer;
}