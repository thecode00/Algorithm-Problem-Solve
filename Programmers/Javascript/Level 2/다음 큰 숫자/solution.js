// https://school.programmers.co.kr/learn/courses/30/lessons/12911?language=javascript

function solution(n) {
  const targetBits = countOneBits(n);
  while (true) {
    n += 1;
    const curOneBits = countOneBits(n);

    if (curOneBits === targetBits) {
      return n;
    }
  }

  return -1;
}

function countOneBits(n) {
  let oneBits = 0;
  // 1은 0001의 비트를 가지고있으므로 1과 AND연산을하면 현재 숫자의 최하위비트(LSB) 즉 맨 오른쪽비트가 1인지 0인지 알수있음
  while (n > 0) {
    oneBits += n & 1;
    n >>= 1;
  }

  return oneBits;
}
