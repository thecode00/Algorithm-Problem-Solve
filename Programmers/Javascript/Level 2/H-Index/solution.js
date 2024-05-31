// https://school.programmers.co.kr/learn/courses/30/lessons/42747?language=javascript

function solution(citations) {
  citations.sort((a, b) => {
    return b - a;
  });

  if (citations.at(-1) >= citations.length) {
    return citations.length;
  }

  for (let idx = 0; idx < citations.length; idx++) {
    if (citations[idx] <= idx) {
      return idx;
    }
  }
  return -1;
}
