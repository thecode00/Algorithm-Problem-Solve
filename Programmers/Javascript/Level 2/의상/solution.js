// https://school.programmers.co.kr/learn/courses/30/lessons/42578?language=javascript

function solution(clothes) {
  const wear = {};
  let answer = 1;

  for (const [_, position] of clothes) {
    if (!wear[position]) {
      // 부위별로 해당 부위를 입지않은 경우를 처리하기위해 1부터 시작
      wear[position] = 1;
    }
    wear[position] += 1;
  }

  for (const count of Object.values(wear)) {
    answer *= count;
  }

  // 모든 부위를 모두 입지않은 경우를 뺌
  return answer - 1;
}
