// https://leetcode.com/problems/assign-cookies/description/

#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int findContentChildren(vector<int> &g, vector<int> &s)
    {
        // Make ascending order
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int result = 0, gIndex = 0, sIndex = 0;
        while (gIndex < g.size() && sIndex < s.size())
        {
            if (g[gIndex] <= s[sIndex])
            {
                result++;
                gIndex++;
            }
            sIndex++;
        }
        return result;
    }
};