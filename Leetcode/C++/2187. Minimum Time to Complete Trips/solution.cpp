// https://leetcode.com/problems/minimum-time-to-complete-trips/description/

#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    long long minimumTime(vector<int> &time, int totalTrips)
    {
        sort(time.begin(), time.end());
        long long int start = 0, end = (long long int)time[0] * totalTrips;
        while (start < end)
        {
            long long int mid = start + (end - start) / 2; // Prevent overflow
            long long int currentTrips = 0;
            for (auto bus : time)
            {
                currentTrips += mid / bus;
            }
            // If currentTrips smallest than totalTrips mid is cant be answer so move start to mid + 1
            if (currentTrips < totalTrips)
            {
                start = mid + 1;
            }
            // If currentTrips greater than or equal totalTrips mid can answer so move end to mid
            else
            {
                end = mid;
            }
        }
        return start; // also end is answer too
    }
};