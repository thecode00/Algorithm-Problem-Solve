// https://leetcode.com/problems/number-complement/description/

#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int findComplement(int num)
    {
        unsigned int n = ~num;
        n <<= __builtin_clz(num);
        n >>= __builtin_clz(num);
        return n;
    }
};