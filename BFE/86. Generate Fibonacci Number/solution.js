// https://bigfrontend.dev/problem/fibonacci-number

/**
 * @param {number} n - non-negative integer
 * @return {number}
 */
function fib(n) {
  const dp = [0, 1];

  for (let idx = 2; idx <= n; idx++) {
    dp.push(dp[idx - 1] + dp[idx - 2]);
  }

  return dp[n];
}
