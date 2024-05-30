// https://school.programmers.co.kr/learn/courses/30/lessons/76502?language=javascript

function solution(s) {
  let answer = 0;
  const length = s.length;
  const parenthesis = new Map([
    [")", "("],
    ["]", "["],
    ["}", "{"],
  ]);

  //  회전별로 올바른 괄호인지 확인
  for (let rotate = 0; rotate < length - 1; rotate++) {
    const stack = [];
    for (let idx = 0; idx < length; idx++) {
      const curParen = s[(idx + rotate) % length];

      // 현재 닫는괄호이고 남아있는 괄호가 맞는 여는괄호인지 확인
      if (stack.length > 0 && parenthesis.has(curParen)) {
        if (stack[stack.length - 1] === parenthesis.get(curParen)) {
          stack.pop();
          continue;
        } else {
          // 올바르지않은 괄호이므로 더이상 탐색할필요가 없음
          break;
        }
      }
      // 여는괄호거나 올바르지않은 닫는괄호일경우 추가
      stack.push(curParen);
    }

    if (stack.length === 0) {
      answer += 1;
    }
  }

  return answer;
}
