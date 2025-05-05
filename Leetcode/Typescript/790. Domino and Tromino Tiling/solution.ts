// https://leetcode.com/problems/domino-and-tromino-tiling/description

function numTilings(n: number): number {
  const MOD = 10 ** 9 + 7;

  if (n === 0) {
    return 1;
  } else if (n === 1) {
    return 1;
  } else if (n === 2) {
    return 2;
  }

  const dp = Array(n + 1);
  dp[0] = 1;
  dp[1] = 1;
  dp[2] = 2;

  /**
   * dp[n] = dp[n - 1] + dp[n - 2] + (dp[n - 3] + dp[n - 4] + ... + dp[0]) * 2
   * = dp[n - 1] + dp[n - 2] + dp[n - 3] + dp[n - 3] + (dp[n - 4] + dp[n - 5] + ... + dp[0]) * 2
   * = dp[n - 1] + dp[n - 3] + (dp[n - 2] + dp[n - 3] + (dp[n - 4] + dp[n - 5] + ... + dp[0]) * 2)
   * = dp[n - 1] + dp[n - 3] + dp[n - 1]
   * = dp[n - 1] * 2 + dp[n - 3]
   */
  // dp[n - 1] = dp[n - 2] + dp[n - 3] + (dp[n - 4] + ... + dp[0]) * 2
  for (let idx = 3; idx <= n; idx++) {
    dp[idx] = (2 * dp[idx - 1] + dp[idx - 3]) % MOD;
  }

  return dp[n];
}
