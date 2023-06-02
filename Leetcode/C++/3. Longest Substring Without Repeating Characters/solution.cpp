// https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
// Time complexity: O(N)

#include <map>
#include <string>

using namespace std;

class Solution
{
public:
    int lengthOfLongestSubstring(string s)
    {
        unordered_map<char, int> used;
        // left = start index of substring
        int left = 0, maxLength = 0;
        for (int idx = 0; idx < s.size(); idx++)
        {
            if (used.find(s[idx]) == used.end())
            {
                used.insert({s[idx], idx});
            }
            // If current char is already used update index
            else
            {
                // Prevent left index move left
                if (left < used[s[idx]] + 1)
                {
                    left = used[s[idx]] + 1;
                }
                used[s[idx]] = idx;
            }
            // Compare maxLength and current substring
            maxLength = max(maxLength, idx - left + 1);
        }
        return maxLength;
    }
};