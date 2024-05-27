// https://school.programmers.co.kr/learn/courses/30/lessons/12909?language=javascript

function solution(s) {
  // 열린 괄호 수
  let openParanthesis = 0;

  for (let p of s) {
    if (p === "(") {
      openParanthesis += 1;
    } else {
      if (openParanthesis <= 0) {
        // 열린 괄호가 앞에 없는데 닫는 괄호가 나올경우 올바르지 않은 괄호
        return false;
      }
      openParanthesis -= 1;
    }
  }

  // 열린 괄호가 남아있는지 체크
  return openParanthesis > 0 ? false : true;
}
