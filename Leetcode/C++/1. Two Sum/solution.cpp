// https://leetcode.com/problems/two-sum/
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> numMap;
        vector<int> answer;
        for (int i = 0; i < nums.size(); i++)
        {
            if (numMap.find(nums[i]) == numMap.end())
            {
                numMap.insert({target - nums[i], i});
            } 
            else {    // Number found
                answer.push_back(numMap[nums[i]]);
                answer.push_back(i);
                return answer;
            }
        }
        return answer;  // Number not found
    }
};