// https://leetcode.com/problems/majority-element/description/

function majorityElement(nums: number[]): number {
  nums.sort((a, b) => a - b);
  return nums[Math.floor(nums.length / 2)];
}
