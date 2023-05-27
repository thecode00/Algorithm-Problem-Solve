// https://leetcode.com/problems/group-anagrams/

#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        vector<vector<string>> result;
        map<string, vector<string>> group;
        for (string s : strs)
        {
            string key = s;
            sort(key.begin(), key.end());
            group[key].push_back(s);
        }

        for (auto value : group)
        {
            result.push_back(value.second);
        }
        return result;
    }
};