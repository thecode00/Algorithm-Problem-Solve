// https://leetcode.com/problems/climbing-stairs/description/

function climbStairs(n: number): number {
  const dp = [0, 1, 2];

  for (let idx = 3; idx <= n; idx++) {
    dp.push(dp[idx - 1] + dp[idx - 2]);
  }

  return dp[n];
}
