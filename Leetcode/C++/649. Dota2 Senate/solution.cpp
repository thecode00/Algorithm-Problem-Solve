// https://leetcode.com/problems/dota2-senate/description/

#include <queue>
#include <string>

using namespace std;

class Solution
{
public:
    string predictPartyVictory(string senate)
    {
        queue<char> q;
        int r = 0, d = 0;
        for (int i = 0; i < senate.size(); i++) // Append to queue and count each team
        {
            q.push(senate[i]);
            if (senate[i] == 'R')
            {
                r += 1;
            }
            else
            {
                d += 1;
            }
        }
        int banR = 0, banD = 0;
        while (r != 0 && d != 0)
        {
            char cur = q.front();
            q.pop();
            if (cur == 'R')
            {
                if (banR > 0) // Dire ban Radiant so cant exercise
                {
                    banR -= 1;
                    r -= 1;
                }
                else // If no ban Radiant, Radiant play next round and ban Dire
                {
                    q.push(cur);
                    banD += 1;
                }
            }
            else
            {
                if (banD > 0) // Radiant ban Dire so cant exercise
                {
                    banD -= 1;
                    d -= 1;
                }
                else // If no ban Dire, Dire play next round and ban Radiant
                {
                    q.push(cur);
                    banR += 1;
                }
            }
        }
        return r == 0 ? "Dire" : "Radiant";
    }
};