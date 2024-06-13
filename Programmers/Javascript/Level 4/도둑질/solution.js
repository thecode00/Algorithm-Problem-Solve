// https://school.programmers.co.kr/learn/courses/30/lessons/42897?language=javascript

function solution(money) {
  const dp1 = Array(money.length).fill(0), // 첫번째집을 턴 경우
    dp2 = Array(money.length).fill(0); // 마지막집을 턴 경우

  dp1[0] = money[0];
  dp1[1] = Math.max(money[0], money[1]);

  for (let idx = 2; idx < money.length - 1; idx++) {
    dp1[idx] = Math.max(dp1[idx - 1], dp1[idx - 2] + money[idx]);
  }

  dp2[1] = money[1];
  for (let idx = 2; idx < money.length; idx++) {
    dp2[idx] = Math.max(dp2[idx - 1], dp2[idx - 2] + money[idx]);
  }

  return Math.max(dp1.at(-2), dp2.at(-1));
}
