// https://leetcode.com/problems/gas-station/

#include <vector>

using namespace std;

class Solution
{
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        int totalGas = 0, curGas = 0, start = 0;
        for (int i = 0; i < gas.size(); i++)
        {
            totalGas += gas[i] - cost[i];
            curGas += gas[i] - cost[i];
            // Previous points has more fuel than when they are start point but travel end current point so previous points cant start point
            if (curGas < 0)
            {
                curGas = 0;
                start = i + 1;
            }
        }
        return totalGas < 0 ? -1 : start;
    }
};

class Solution // TLE: O(N ^ 2)
{
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        for (int start = 0; start < gas.size(); start++)
        {
            int fuel = 0, cur;
            bool canTravel = true;
            for (int i = 0; i < gas.size(); i++)
            {
                cur = (start + i) % gas.size();
                fuel += gas[cur] - cost[cur];
                if (fuel < 0)
                {
                    canTravel = false;
                    break;
                }
            }
            if (canTravel)
            {
                return start;
            }
        }
        return -1;
    }
};