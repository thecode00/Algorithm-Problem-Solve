// https://leetcode.com/problems/koko-eating-bananas/description/

#include <algorithm>
#include <vector>
using namespace std;

class Solution
{
public:
    int minEatingSpeed(vector<int> &piles, int h)
    {
        int start = 1, end = *max_element(piles.begin(), piles.end());
        if (piles.size() == h)
        {
            return end;
        }
        while (start < end)
        {
            int mid = start + (end - start) / 2; // Prevent overflow
            int spendTime = 0;
            for (auto banana : piles)
            {
                spendTime += banana / mid;
                if (banana % mid != 0)
                {
                    spendTime += 1;
                }
            }
            if (spendTime > h) // If spend_time bigger than h mid cant be answer so move start to mid + 1
            {
                start = mid + 1;
            }
            else // If spend_time <= h, mid can be answer so move end to mid
            {
                end = mid;
            }
        }
        return start;
    }
};