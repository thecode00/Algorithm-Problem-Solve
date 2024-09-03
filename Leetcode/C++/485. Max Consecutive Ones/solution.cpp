// https://leetcode.com/problems/max-consecutive-ones/description/

class Solution
{
public:
    int findMaxConsecutiveOnes(vector<int> &nums)
    {
        int maxCons = 0;
        int curCons = 0;

        for (auto cur : nums)
        {
            if (cur == 1)
            {
                curCons += 1;
            }
            else
            {
                curCons = 0;
            }
            maxCons = max(curCons, maxCons);
        }

        return maxCons;
    }
};