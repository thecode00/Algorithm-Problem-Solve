// https://school.programmers.co.kr/learn/courses/30/lessons/12973?language=javascript

function solution(s) {
  const stack = [];

  for (let char of s) {
    // 제거할수있는 알파벳 짝이 있다면 바로바로 제거
    if (stack.length > 0 && stack[stack.length - 1] === char) {
      stack.pop();
    } else {
      stack.push(char);
    }
  }

  return stack.length > 0 ? 0 : 1;
}
