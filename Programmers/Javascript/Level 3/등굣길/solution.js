// https://school.programmers.co.kr/learn/courses/30/lessons/42898?language=javascript

function solution(m, n, puddles) {
  const dp = Array.from(Array(n + 1), () => Array(m + 1).fill(0));
  const MOD = 1000000007;

  dp[1][1] = 1;

  for (const [x, y] of puddles) {
    dp[y][x] = -1;
  }

  for (let y = 1; y < n + 1; y++) {
    for (let x = 1; x < m + 1; x++) {
      if (dp[y][x] === -1) {
        // 웅덩이는 다음 경로의 계산을 위해 0으로 변환
        dp[y][x] = 0;
        continue;
      }

      if (y > 1) {
        dp[y][x] = (dp[y][x] + dp[y - 1][x]) % MOD;
      }

      if (x > 1) {
        dp[y][x] = (dp[y][x] + dp[y][x - 1]) % MOD;
      }
    }
  }

  return dp[n][m];
}
