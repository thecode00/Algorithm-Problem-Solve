// https://school.programmers.co.kr/learn/courses/30/lessons/87390?language=javascript

function solution(n, left, right) {
  const answer = [];

  for (let idx = left; idx <= right; idx++) {
    // Math.floor(idx / n)는 행, idx % n은 열 번호
    answer.push(Math.max(Math.floor(idx / n), idx % n) + 1);
  }
  return answer;
}
