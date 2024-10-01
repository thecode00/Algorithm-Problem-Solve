// https://leetcode.com/problems/house-robber/description/

function rob(nums: number[]): number {
  const dp = [nums[0]];

  for (let idx = 1; idx < nums.length; idx++) {
    if (idx === 1) {
      dp.push(Math.max(nums[0], nums[1]));
      continue;
    }

    dp.push(Math.max(dp[idx - 1], dp[idx - 2] + nums[idx]));
  }

  return dp[nums.length - 1];
}
