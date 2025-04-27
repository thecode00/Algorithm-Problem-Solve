// https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/description

function countSubarrays(nums: number[]): number {
  let count = 0;

  for (let idx = 0; idx < nums.length - 2; idx++) {
    if ((nums[idx] + nums[idx + 2]) * 2 === nums[idx + 1]) {
      count += 1;
    }
  }

  return count;
}
