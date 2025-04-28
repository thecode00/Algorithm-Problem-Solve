// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description

function countSubarrays(nums: number[], minK: number, maxK: number): number {
  let minIndex = -1;
  let maxIndex = -1;
  let invalidIndex = -1;
  let count = 0;

  for (let idx = 0; idx < nums.length; idx++) {
    const num = nums[idx];

    // Invalid index
    if (num < minK || maxK < num) {
      invalidIndex = idx;
    }

    if (num === minK) {
      minIndex = idx;
    }

    if (num === maxK) {
      maxIndex = idx;
    }

    // minIndex and maxIndex represent the most recent positions of minK and maxK, respectively.
    // Therefore, subArrStart is the start of the smallest valid subarray ending at the current index.
    // so we can calculate the number of subarray includes valid subarrays
    const subArrStart = Math.min(minIndex, maxIndex);
    if (invalidIndex < subArrStart) {
      count += subArrStart - invalidIndex;
    }
  }

  return count;
}
