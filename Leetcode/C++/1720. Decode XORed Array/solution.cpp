// https://leetcode.com/problems/decode-xored-array/description/

class Solution
{
public:
    vector<int> decode(vector<int> &encoded, int first)
    {
        /*
        a = b ^ c
        c ^ a = c ^ (b ^ c) = c ^ c ^ b = 0 ^ b = b
        b = c ^ a
        */
        vector<int> result;
        result.emplace_back(first);
        for (auto num : encoded)
        {
            result.emplace_back(result.back() ^ num);
        }
        return result;
    }
};