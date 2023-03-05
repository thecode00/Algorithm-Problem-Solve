// https://leetcode.com/problems/jump-game-iv/description/

#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution
{
public:
    int minJumps(vector<int> &arr)
    {
        int len = arr.size();
        unordered_map<int, vector<int>> index_hash;
        for (int i = 0; i < len; i++)
        {
            index_hash[arr[i]].push_back(i);
        }

        vector<int> dp(len, -1); // Initialize vector -1
        dp[0] = 0;
        queue<int> q;
        q.push(0); // Strat point
        while (!(q.empty()))
        {
            for (int i = q.size(); 0 < i; i--)
            {
                int cur = q.front();
                if (cur == len - 1) // Reach
                {
                    return dp[len - 1];
                }
                vector<int> &next = index_hash[arr[cur]];
                // Combine into next vector and process at the same time
                next.push_back(cur - 1);
                next.push_back(cur + 1);
                for (int j = 0; j < next.size(); j++)
                {
                    if (next[j] >= 0 && next[j] < len && dp[next[j]] == -1)
                    {
                        q.push(next[j]);
                        dp[next[j]] = dp[cur] + 1;
                    }
                }
                next = {}; // For prevent revisit clear vector
                q.pop();
            }
        }
        return 0;
    }
};