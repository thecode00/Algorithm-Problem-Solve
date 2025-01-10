// https://leetcode.com/problems/two-sum/description/

function twoSum(nums: number[], target: number): number[] {
  const index = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    if (index.has(target - nums[i])) {
      return [index.get(target - nums[i]), i];
    }
    index.set(nums[i], i);
  }
}
