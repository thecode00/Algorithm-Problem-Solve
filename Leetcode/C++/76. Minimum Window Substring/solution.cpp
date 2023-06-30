// https://leetcode.com/problems/minimum-window-substring/description/

#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    string minWindow(string s, string t)
    {
        unordered_map<char, int> subAlpha;
        for (auto c : t)
        { // Count t char
            subAlpha[c] += 1;
        }
        /*
         * start, end = minimum substring index
         * left = current window left index
         * diff = Characters numbers that are in "t" but not present in the window.
         */
        int left = 0, start = -1, end = -1, diff = t.size();
        for (int right = 0; right < s.size(); right++)
        {
            diff -= subAlpha[s[right]] > 0;
            subAlpha[s[right]] -= 1;

            if (diff == 0) // When substring in window
            {
                while (left < right && subAlpha[s[left]] < 0) // Find minimum substring in window
                {
                    subAlpha[s[left]] += 1;
                    left += 1;
                }

                if (start == -1 || right - left < end - start) // Compare substring size
                {
                    start = left;
                    end = right;
                }
                // Check finish move left index
                subAlpha[s[left]] += 1;
                diff += 1;
                left += 1;
            }
        }
        if (start == -1) // There is no substring
        {
            return "";
        }
        string result(s.begin() + start, s.begin() + end + 1);
        return result;
    }
};