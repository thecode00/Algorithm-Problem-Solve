// https://leetcode.com/problems/boats-to-save-people/description/

#include <algorithm>
#include <vector>

using namespace std;

class Solution
{
public:
    int numRescueBoats(vector<int> &people, int limit)
    {
        sort(people.begin(), people.end());
        int left = 0, right = people.size() - 1;
        int count = 0;
        while (left <= right)
        {
            // If boat can carry heaviest people and lightest people move left pointer
            if (people[left] + people[right] <= limit)
            {
                left += 1;
            }
            right -= 1;
            count += 1;
        }
        return count;
    }
};