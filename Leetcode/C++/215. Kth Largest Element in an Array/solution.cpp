
#include <vector>
#include <queue>

using namespace std;

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        priority_queue<int> pq;
        for (int &num : nums)
        {
            pq.push(-num);
        }

        for (int i = 0; i < (nums.size() - k); i++)
        {
            pq.pop();
        }
        return -pq.top();
    }
};

class Solution
{
public:
    int findKthLargest(vector<int> &nums, int k)
    {
        sort(nums.rbegin(), nums.rend());
        return nums[k - 1];
    }
};