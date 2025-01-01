// https://leetcode.com/problems/minimum-cost-for-tickets/description

function mincostTickets(days: number[], costs: number[]): number {
  const daySet = new Set(days);
  const dp = Array.from({ length: 366 }, (_) => 0);

  for (let day = 1; day <= 365; day++) {
    if (daySet.has(day)) {
      dp[day] = Math.min(
        dp[day - 1] + costs[0],
        dp[Math.max(0, day - 7)] + costs[1],
        dp[Math.max(0, day - 30)] + costs[2]
      );
    } else {
      dp[day] = dp[day - 1];
    }
  }

  return dp[365];
}
