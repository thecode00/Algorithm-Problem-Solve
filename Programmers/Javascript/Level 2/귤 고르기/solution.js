// https://school.programmers.co.kr/learn/courses/30/lessons/138476?language=javascript

function solution(k, tangerine) {
  const tangerineCount = new Map();
  let answer = 0;

  // 귤 크기별 개수를 센 후 가장 개수가 많은 종류의 귤만 써서 최대한 종류를 적게 씀
  for (const t of tangerine) {
    if (!tangerineCount.has(t)) {
      tangerineCount.set(t, 0);
    }

    tangerineCount.set(t, tangerineCount.get(t) + 1);
  }

  const sortedCount = Array.from(tangerineCount.values()).sort((a, b) => b - a);

  for (const count of sortedCount) {
    k -= count;
    answer += 1;
    if (k <= 0) {
      break;
    }
  }
  return answer;
}
