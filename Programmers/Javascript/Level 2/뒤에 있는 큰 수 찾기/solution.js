// https://school.programmers.co.kr/learn/courses/30/lessons/154539?language=javascript

function solution(numbers) {
  const stack = [];
  const result = Array(numbers.length).fill(-1);

  numbers.forEach((num, idx) => {
    while (stack.length > 0) {
      const [prevNum, prevIdx] = stack.pop();
      // 현재 숫자가 가장 가까운 큰수가 되는 숫자들 탐색
      if (num > prevNum) {
        result[prevIdx] = num;
      } else {
        stack.push([prevNum, prevIdx]);
        break;
      }
    }
    stack.push([num, idx]);
  });
  return result;
}
