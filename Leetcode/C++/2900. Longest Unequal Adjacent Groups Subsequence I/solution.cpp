// https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description

#include <string>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<string> getLongestSubsequence(vector<string> &words, vector<int> &groups)
    {
        vector<string> result = {};

        int searchLength = words.size() - 1;
        int idx = 0;
        while (idx < words.size())
        {
            result.emplace_back(words[idx]);

            while (idx < searchLength && groups[idx] == groups[idx + 1])
            {
                idx += 1;
            }
            idx += 1;
        }

        return result;
    }
};