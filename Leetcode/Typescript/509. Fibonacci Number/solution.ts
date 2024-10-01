// https://leetcode.com/problems/fibonacci-number/description/

function fib(n: number): number {
  const dp = [0, 1];

  for (let idx = 2; idx <= n; idx++) {
    dp.push(dp[idx - 1] + dp[idx - 2]);
  }

  return dp[n];
}
