// https://leetcode.com/problems/longest-repeating-character-replacement/description/

#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    int characterReplacement(string s, int k)
    {
        int longest = 0, left = 0;
        unordered_map<char, int> counter;
        for (int right = 0; right < s.size(); right++)
        {
            counter[s[right]] += 1;
            int mostChar = mostCommon(counter);
            if (mostChar + k < right - left + 1) // Most common char cant cover left, rigth range with replacement move left index
            {
                counter[s[left]] -= 1;
                left += 1;
            }
            longest = max(longest, right - left + 1);
        }
        return longest;
    }

    int mostCommon(unordered_map<char, int> &counter) // Find mostCommon char in left, right range
    {
        int maxCount = INT_MIN;
        for (auto &pair : counter)
        {
            if (maxCount < pair.second)
            {
                maxCount = pair.second;
            }
        }
        return maxCount;
    }
};