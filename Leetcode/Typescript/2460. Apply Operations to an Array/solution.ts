// https://leetcode.com/problems/apply-operations-to-an-array/description

function applyOperations(nums: number[]): number[] {
  let insertIdx = 0;

  for (let idx = 0; idx < nums.length - 1; idx++) {
    if (nums[idx] === nums[idx + 1]) {
      nums[idx] *= 2;
      nums[idx + 1] = 0;
    }
  }

  for (let idx = 0; idx < nums.length; idx++) {
    if (nums[idx] !== 0) {
      [nums[idx], nums[insertIdx]] = [nums[insertIdx], nums[idx]];
      insertIdx += 1;
    }
  }

  return nums;
}
