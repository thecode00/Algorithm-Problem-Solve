// https://school.programmers.co.kr/learn/courses/30/lessons/12900?language=javascript

function solution(n) {
  const dp = [0, 1, 2];
  // 왠지는 모르겠는데 MOD변수를 사용해서 나머지를 구하면 시간초과가 남 문제의 버그인듯
  //   const MOD = 1000000007;

  for (let idx = 3; idx <= n; idx++) {
    dp.push((dp[idx - 1] + dp[idx - 2]) % 1000000007);
  }
  return dp[n];
}
