// https://leetcode.com/problems/sort-colors/description/

/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
  const pivot = 1;
  let idx = 0;
  let start = 0;
  let end = nums.length - 1;

  // Split 3, [less than pivot, equal pivot, greater than pivot]
  while (idx <= end) {
    if (nums[idx] < pivot) {
      [nums[idx], nums[start]] = [nums[start], nums[idx]];
      start += 1;
      idx += 1;
    } else if (nums[idx] === pivot) {
      idx += 1;
    } else {
      [nums[idx], nums[end]] = [nums[end], nums[idx]];
      end -= 1;
    }
  }
}
