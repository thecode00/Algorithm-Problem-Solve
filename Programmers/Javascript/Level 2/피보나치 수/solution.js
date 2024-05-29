// https://school.programmers.co.kr/learn/courses/30/lessons/12945?language=javascript

function solution(n) {
  if (n <= 1) {
    return n;
  }
  const dp = new Array(n + 1);
  (dp[0] = 0), (dp[1] = 1);

  for (let idx = 2; idx <= n; idx++) {
    dp[idx] = (dp[idx - 1] + dp[idx - 2]) % 1234567;
  }
  return dp[n];
}
