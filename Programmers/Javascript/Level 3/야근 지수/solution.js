// https://school.programmers.co.kr/learn/courses/30/lessons/12927?language=javascript

function solution(n, works) {
  const totalWorkTime = works.reduce((prev, cur) => prev + cur, 0);
  let answer = 0;

  if (totalWorkTime <= n) {
    return answer;
  }

  works.sort((a, b) => b - a);

  // 가장 오래걸리는 작업부터 줄여나감
  while (n > 0) {
    const maxWork = works[0];

    for (let idx = 0; idx < works.length; idx++) {
      if (works[idx] !== maxWork || n <= 0) {
        break;
      }

      works[idx] -= 1;
      n -= 1;
    }
  }

  return works.reduce((prev, cur) => prev + cur ** 2, 0);
}
