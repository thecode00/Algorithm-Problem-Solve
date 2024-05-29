// https://school.programmers.co.kr/learn/courses/30/lessons/12914?language=javascript

function solution(n) {
  const dp = Array(n + 1);
  dp[0] = 1;
  dp[1] = 1;

  for (let idx = 2; idx <= n; idx++) {
    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 1234567;
  }

  return dp[n];
}
