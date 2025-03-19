// https://leetcode.com/problems/coin-change-ii/description/

function change(amount: number, coins: number[]): number {
  const dp = Array.from({ length: amount + 1 }, (_) => 0);
  dp[0] = 1;

  for (const coin of coins) {
    for (let i = coin; i <= amount; i++) {
      dp[i] += dp[i - coin];
    }
  }

  return dp[amount];
}
