// https://leetcode.com/problems/climbing-stairs/description/

// Bottom-up
function climbStairs(n: number): number {
  const dp = [0, 1, 2];

  for (let idx = 3; idx <= n; idx++) {
    dp.push(dp[idx - 1] + dp[idx - 2]);
  }

  return dp[n];
}

// Memoization
function climbStairs(n: number): number {
  return memoization(
    n,
    Array.from({ length: n + 1 }, (_) => 0)
  );
}

function memoization(n: number, dp: number[]) {
  if (n <= 2) {
    return n;
  }

  if (dp[n] === 0) {
    dp[n] = memoization(n - 1, dp) + memoization(n - 2, dp);
  }

  return dp[n];
}
