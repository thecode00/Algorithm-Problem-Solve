// https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/cpp

#include <climits>
#include <vector>

using namespace std;

int findSmallest(vector<int> list)
{
    int min_num = INT_MAX;
    for (int num : list)
    {
        if (num < min_num)
        {
            min_num = num;
        }
    }
    return min_num;
}