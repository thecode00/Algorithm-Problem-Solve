// https://school.programmers.co.kr/learn/courses/30/lessons/12941?language=javascript#

function solution(A, B) {
  A.sort((a, b) => {
    return a - b;
  });
  B.sort((a, b) => {
    return b - a;
  });

  let answer = 0;
  const length = A.length;

  for (let idx = 0; idx < length; idx++) {
    answer += A[idx] * B[idx];
  }

  return answer;
}
