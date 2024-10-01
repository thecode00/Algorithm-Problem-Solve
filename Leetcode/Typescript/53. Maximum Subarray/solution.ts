// https://leetcode.com/problems/maximum-subarray/description/

function maxSubArray(nums: number[]): number {
  let maxNum = nums[0];

  for (let idx = 1; idx < nums.length; idx++) {
    if (nums[idx - 1] > 0) {
      nums[idx] += nums[idx - 1];
    }
    maxNum = Math.max(maxNum, nums[idx]);
  }

  return maxNum;
}
