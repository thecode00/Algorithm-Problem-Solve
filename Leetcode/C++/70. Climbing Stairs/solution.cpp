// https://leetcode.com/problems/climbing-stairs/

#include <vector>

using namespace std;

class Solution // Bottom-up
{
public:
    int climbStairs(int n)
    {
        if (n == 1)
        {
            return n;
        }
        int a = 1, b = 2, temp;
        for (int i = 2; i < n; i++)
        {
            temp = a;
            a = b;
            b = temp + b;
        }
        return b;
    }
};