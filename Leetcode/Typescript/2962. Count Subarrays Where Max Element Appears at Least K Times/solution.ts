// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description

function countSubarrays(nums: number[], k: number): number {
  const maxNum = Math.max(...nums);
  let count = 0;
  let queue: number[] = [];

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === maxNum) {
      queue.push(i);
    }

    // For each index, add the number of subarrays ending at that index which have exactly k occurrences of the maximum element.
    if (queue.length >= k) {
      const startIdx = queue[queue.length - k];
      count += startIdx + 1;
    }
  }

  return count;
}
