// https://leetcode.com/problems/array-partition/description/

function arrayPairSum(nums: number[]): number {
  nums.sort((a, b) => {
    return a - b;
  });

  let answer = 0;

  for (let idx = 0; idx < nums.length; idx += 2) {
    answer += Math.min(nums[idx], nums[idx + 1]);
  }

  return answer;
}
