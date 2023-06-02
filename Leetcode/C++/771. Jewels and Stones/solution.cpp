// https://leetcode.com/problems/jewels-and-stones/

#include <string>
#include <set>

using namespace std;

class Solution
{
public:
    int numJewelsInStones(string jewels, string stones)
    {
        set<char> jewelSet;
        int count = 0;
        for (char jewel : jewels)
        {
            jewelSet.insert(jewel);
        }
        for (char stone : stones)
        {
            if (jewelSet.find(stone) != jewelSet.end())
            {
                count += 1;
            }
        }
        return count;
    }
};