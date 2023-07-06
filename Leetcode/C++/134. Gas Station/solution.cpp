// https://leetcode.com/problems/gas-station/

#include <vector>

using namespace std;

class Solution
{
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        int gasTotal = 0, costTotal = 0;
        for (int i = 0; i < gas.size(); i++)
        {
            gasTotal += gas[i];
            costTotal += cost[i];
        }

        if (gasTotal < costTotal)
        {
            return -1;
        }

        int start = 0, fuel = 0;
        // Find start index
        for (int i = 0; i < gas.size(); i++)
        {
            fuel += gas[i] - cost[i];
            if (fuel < 0)
            {
                fuel = 0;
                start = i + 1;
            }
        }
        return start;
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