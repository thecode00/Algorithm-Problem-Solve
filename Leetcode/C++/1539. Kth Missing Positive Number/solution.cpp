// https://leetcode.com/problems/kth-missing-positive-number/

#include <vector>

using namespace std;

class Solution
{
public:
    int findKthPositive(vector<int> &arr, int k)
    {
        int num = 1, index = 0;
        while (k > 0)
        {
            if (index < arr.size() && arr[index] == num)
            {
                index += 1;
            }
            else
            {
                k -= 1;
            }
            num += 1;
        }
        return num - 1; // num - 1 is answer because num is added to num at the end of the while loop.
    }
};