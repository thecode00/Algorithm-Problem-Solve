// https://school.programmers.co.kr/learn/courses/30/lessons/12939?language=javascript

function solution(s) {
  // 처음엔 maxNum을 설정할 때 -Infinity가 아닌 Number.MIN_VALUE를 썼었다.
  // Number.MIN_VALUE는 음수로 나타낼 수 있는 최저값이 아닌 5e-324이므로 음수 최저값을 나타내려면 -Infinity를 써야한다.
  let minNum = Number.MAX_VALUE,
    maxNum = -Infinity;

  for (let strNum of s.split(" ")) {
    const num = parseInt(strNum);

    minNum = Math.min(minNum, num);
    maxNum = Math.max(maxNum, num);
  }

  return `${minNum} ${maxNum}`;
}
