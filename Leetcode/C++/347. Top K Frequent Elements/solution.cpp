// https://leetcode.com/problems/top-k-frequent-elements/

#include <vector>
#include <map>
#include <queue>

using namespace std;

class Solution
{
public:
    vector<int> topKFrequent(vector<int> &nums, int k)
    {
        unordered_map<int, int> counter;
        // Count elements frequent
        for (int num : nums)
        {
            if (counter.find(num) == counter.end())
            {
                counter[num] = 1;
            }
            else
            {
                counter[num] += 1;
            }
        }
        // priority_queue top returns largest value so push elements count to prirority_queue
        priority_queue<pair<int, int>> mostFrequent;
        for (auto pair : counter)
        {
            mostFrequent.push({pair.second, pair.first});
        }

        vector<int> result;
        for (k; k > 0; k--)
        {
            // Get most frequent element
            if (!mostFrequent.empty())
            {
                int element = mostFrequent.top().second;
                mostFrequent.pop();
                result.push_back(element);
            }
            else
            {
                break;
            }
        }
        return result;
    }
};