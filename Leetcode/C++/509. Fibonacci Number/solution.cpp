// https://leetcode.com/problems/fibonacci-number/description/

#include <vector>

using namespace std;

class Solution // Bottom-up
{
public:
    int fib(int n)
    {
        if (n <= 1)
        {
            return n;
        }
        vector<int> fb;
        fb.push_back(0);
        fb.push_back(1);

        for (int i = 2; i <= n; i++)
        {
            fb.push_back(fb[i - 2] + fb[i - 1]);
        }
        return fb[n];
    }
};

class Solution // Top-down
{
public:
    vector<int> fb = {0, 1};
    int fib(int n)
    {
        if (n <= 1)
        {
            return n;
        }

        if (n < fb.size())
        {
            return fb[n];
        }
        fb.push_back(fib(n - 1) + fib(n - 2));
        return fb[n];
    }
};

class Solution // Save space use two variables, Space complexity: O(1);
{
public:
    int fib(int n)
    {
        if (n == 0)
        {
            return 0;
        }
        int a = 0, b = 1, temp;
        for (int i = 1; i < n; i++)
        {
            temp = a;
            a = b;
            b = temp + b;
        }
        return b;
    }
};
