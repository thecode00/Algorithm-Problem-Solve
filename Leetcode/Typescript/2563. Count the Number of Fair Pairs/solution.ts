// https://leetcode.com/problems/count-the-number-of-fair-pairs/description

function countFairPairs(nums: number[], lower: number, upper: number): number {
  nums.sort((a, b) => a - b);

  let pairs = 0;
  for (let idx = 0; idx < nums.length; idx++) {
    const lowerIdx = lowerBound(nums, lower - nums[idx], idx + 1);
    const upperIdx = upperBound(nums, upper - nums[idx], idx + 1);

    pairs += upperIdx - lowerIdx;
  }

  return pairs;
}

function lowerBound(nums: number[], target: number, start: number): number {
  let left = start,
    right = nums.length;
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}

function upperBound(nums: number[], target: number, start: number): number {
  let left = start,
    right = nums.length;
  while (left < right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] <= target) {
      left = mid + 1;
    } else {
      right = mid;
    }
  }
  return left;
}
