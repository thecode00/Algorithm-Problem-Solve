// https://school.programmers.co.kr/learn/courses/30/lessons/92335?language=javascript

function solution(n, k) {
  let answer = 0;
  const convertedNumber = convertBase(n, k).split("0");
  convertedNumber.sort((a, b) => a - b);

  for (const num of convertedNumber) {
    if (!isNaN(num) && num > 1) {
      let isPrime = true;

      // 소수 판별기법, 약수는 자신의 짝이 있기때문에 자신의 짝이 자기자신인 제곱근까지만 탐색
      for (let n = 2; n <= Math.sqrt(num); n++) {
        if (num % n === 0) {
          isPrime = false;
          break;
        }
      }
      answer += isPrime;
    }
  }

  return answer;
}

/**
 * 숫자를 진수 변환하여 문자열로 변환해줌
 * @param {number} n 진수 변환을 할 숫자
 * @param {number} base 목표 진법
 * @return {string} 진수 변환을 한 숫자를 문자열로 반환
 */
function convertBase(n, base) {
  const bits = [];

  while (n / base >= 1) {
    bits.push(n % base);
    n = Math.floor(n / base);
  }

  bits.push(n);
  return bits.reverse().join("");
}
