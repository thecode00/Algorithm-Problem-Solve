// https://leetcode.com/problems/number-of-ways-to-split-array/description

function waysToSplitArray(nums: number[]): number {
  let total = nums.reduce((acc, current) => acc + current, 0);
  let sumLeft = 0;
  let validCount = 0;

  for (let idx = 0; idx < nums.length - 1; idx++) {
    sumLeft += nums[idx];

    if (total - sumLeft <= sumLeft) {
      validCount += 1;
    }
  }

  return validCount;
}
