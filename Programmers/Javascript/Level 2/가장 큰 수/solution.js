// https://school.programmers.co.kr/learn/courses/30/lessons/42746?language=javascript

function solution(numbers) {
  numbers = numbers
    .map((value) => {
      // 자릿수로 비교를하기위해 문자열로 변환
      return String(value);
    })
    .sort((a, b) => {
      // 합친 숫자값을 크기순으로 정렬하기위해 단항 연산자로 정수로 바꾼다음 비교
      return +(b + a) - +(a + b);
    });

  const result = numbers.join("");
  // "000"같은 경우를 방지하기위해 정수로 변환하여 검사
  return +result === 0 ? "0" : result;
}
