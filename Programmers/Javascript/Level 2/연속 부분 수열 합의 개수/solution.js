// https://school.programmers.co.kr/learn/courses/30/lessons/131701?language=javascript

function solution(elements) {
  const length = elements.length;
  // dp[a][b]는 시작 부분이 b인 길이가 a인 연속 부분 수열의 합
  const dp = Array.from(Array(length), () => Array(length));
  const sumList = new Set(elements);

  for (let y = 0; y < length; y++) {
    for (let x = 0; x < length; x++) {
      if (y === 0) {
        dp[y][x] = elements[x];
        continue;
      }

      const newSum = dp[y - 1][x] + elements[(x + y) % length];
      sumList.add(newSum);
      dp[y][x] = newSum;
    }
  }

  return sumList.size;
}
