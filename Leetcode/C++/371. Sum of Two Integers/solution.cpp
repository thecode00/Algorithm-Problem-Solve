// https://leetcode.com/problems/sum-of-two-integers/

#include <bitset>

using namespace std;

class Solution // Implement adder
{
public:
    int getSum(int a, int b)
    {
        bitset<32> bitsA(a), bitsB(b), bitsResult(0);
        int carry = 0;
        for (int i = 0; i < 32; i++)
        {
            int Q1 = bitsA[i] ^ bitsB[i];
            int Q2 = bitsA[i] & bitsB[i];
            int Q3 = Q1 & carry;
            int sum = Q1 ^ carry;
            carry = Q2 | Q3;
            bitsResult[i] = sum;
        }
        return bitsResult.to_ulong();
    }
};

class Solution
{
public:
    int getSum(int a, int b)
    {
    }
};