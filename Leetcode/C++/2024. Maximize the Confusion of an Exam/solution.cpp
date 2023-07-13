// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description/

#include <vector>
#include <string>

using namespace std;

class Solution
{
public:
    int maxConsecutiveAnswers(string answerKey, int k)
    {
        return max(findMax(answerKey, k, 'T'), findMax(answerKey, k, 'F'));
    }
    // If diffKey == 'T' change 'T' to 'F'
    int findMax(string &answerKey, int k, char diffKey)
    {
        int left = 0, maxCount = 0, curK = k;
        for (int right = 0; right < answerKey.size(); right++)
        {
            if (answerKey[right] == diffKey)
            {
                curK--;
            }
            // Use all change, move left index to next (diffKey index + 1)
            while (curK < 0)
            {
                if (answerKey[left] == diffKey)
                {
                    curK++;
                }
                left++;
            }
            maxCount = max(maxCount, right - left + 1);
        }
        return maxCount;
    }
};