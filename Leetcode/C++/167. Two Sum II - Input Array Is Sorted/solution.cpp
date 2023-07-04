// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/980465431/

#include <vector>

using namespace std;

class Solution // Two pointer: O(N)
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int left = 0, right = numbers.size() - 1;
        int total;
        while (left < right)
        {
            total = numbers[left] + numbers[right];
            if (total > target)
            {
                right--;
            }
            else if (total < target)
            {
                left++;
            }
            else
            {
                // Make 1-index
                left++;
                right++;
                break;
            }
        }
        return {left, right};
    }
};

class Solution // Binary search
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        int left, right, mid, num;
        for (int i = 0; i < numbers.size(); i++)
        {
            num = numbers[i];
            left = i + 1;
            right = numbers.size() - 1;
            while (left <= right)
            {
                mid = left + (right - left) / 2;
                if (num + numbers[mid] > target)
                {
                    right = mid - 1;
                }
                else if (num + numbers[mid] < target)
                {
                    left = mid + 1;
                }
                else
                {
                    // Make 1-index and return answer
                    return {i + 1, mid + 1};
                }
            }
        }
        return {-1, -1}; // Dummy data problem guarantee there is one answer
    }
};