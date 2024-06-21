// https://leetcode.com/problems/array-partition/description/

class Solution {
    public int arrayPairSum(int[] nums) {
        Arrays.sort(nums);
        int answer = 0;

        for (int idx = 0; idx < nums.length; idx += 2){
            answer += nums[idx];
        }

        return answer;
    }
}