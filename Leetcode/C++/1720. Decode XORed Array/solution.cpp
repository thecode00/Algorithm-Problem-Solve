// https://leetcode.com/problems/decode-xored-array/description/

class Solution
{
public:
    vector<int> decode(vector<int> &encoded, int first)
    {
        // a = b ^ c, b = a ^ c
        vector<int> result;
        result.emplace_back(first);
        for (auto num : encoded)
        {
            result.emplace_back(result.back() ^ num);
        }
        return result;
    }
};