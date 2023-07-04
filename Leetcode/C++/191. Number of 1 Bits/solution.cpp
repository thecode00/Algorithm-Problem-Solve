// https://leetcode.com/problems/number-of-1-bits/description/

#include <stdint.h>

using namespace std;

class Solution
{
public:
    int hammingWeight(uint32_t n)
    {
        int count = 0;
        while (n > 0)
        {
            count += n % 2;
            n >>= 1;
        }
        return count;
    }
};

class Solution // Use gcc compiler built-in function
{
public:
    int hammingWeight(uint32_t n)
    {
        return __builtin_popcount(n);
    }
};