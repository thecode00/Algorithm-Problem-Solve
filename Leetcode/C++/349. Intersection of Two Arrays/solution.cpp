// https://leetcode.com/problems/intersection-of-two-arrays/description/

#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        set<int> setNums1;
        // Delete duplicate elements in nums1
        for (auto num : nums1)
        {
            setNums1.insert(num);
        }
        sort(nums2.begin(), nums2.end());

        vector<int> result;
        int left, right, mid;
        // Find intersect using binary search
        for (auto num : setNums1)
        {
            left = 0;
            right = nums2.size() - 1;
            while (left <= right)
            {
                mid = left + (right - left) / 2;
                if (nums2[mid] > num)
                {
                    right = mid - 1;
                }
                else if (nums2[mid] < num)
                {
                    left = mid + 1;
                }
                else
                {
                    result.push_back(num);
                    break;
                }
            }
        }
        return result;
    }
};

class Solution // Two pointer
{
public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2)
    {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());
        // Use set for delete duplicate intersect elements
        set<int> intersect;
        int index1 = 0, index2 = 0;
        while (index1 < nums1.size() && index2 < nums2.size())
        {
            if (nums1[index1] == nums2[index2])
            {
                intersect.insert(nums1[index1]);
                index1++;
                index2++;
            }
            else if (nums1[index1] > nums2[index2])
            {
                index2++;
            }
            else
            {
                index1++;
            }
        }

        vector<int> result;
        for (auto num : intersect)
        {
            result.push_back(num);
        }
        return result;
    }
};