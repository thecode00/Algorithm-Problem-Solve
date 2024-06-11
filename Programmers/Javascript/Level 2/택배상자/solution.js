// https://school.programmers.co.kr/learn/courses/30/lessons/131704?language=javascript

function solution(order) {
  const assist = [];

  let lastBox = 0, // 마지막으로 어딘가에 실린 박스
    answer = 0;

  for (const box of order) {
    if (lastBox < box) {
      // 박스가 트럭에 실려야 할때 현재 박스보다 작은 박스들을 보조 컨베이어에 넣음
      for (let idx = lastBox + 1; idx < box; idx++) {
        assist.push(idx);
      }
      answer += 1;
      lastBox = box;
    } else {
      // 박스가 보조 컨베이어에 실려있는 경우
      if (assist.at(-1) === box) {
        answer += 1;
        assist.pop();
      } else {
        return answer;
      }
    }
  }
  return answer;
}
