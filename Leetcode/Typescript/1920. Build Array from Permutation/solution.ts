// https://leetcode.com/problems/build-array-from-permutation/description

function buildArray(nums: number[]): number[] {
  const answer = Array(nums.length);

  for (let idx = 0; idx < nums.length; idx++) {
    answer[idx] = nums[nums[idx]];
  }

  return answer;
}
