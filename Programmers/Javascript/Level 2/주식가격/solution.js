// https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=javascript

function solution(prices) {
  const stocks = [];
  const length = prices.length;
  const answer = Array(length).fill(0);

  prices.forEach((price, idx) => {
    // 현재 주식이 하락한 가격인 주식들 탐색
    while (stocks.length > 0 && stocks[stocks.length - 1][0] > price) {
      const [_, prevIdx] = stocks.pop();

      answer[prevIdx] = idx - prevIdx;
    }

    stocks.push([price, idx]);
  });

  // 끝까지 떨어지지않은 주식들 처리
  while (stocks.length > 0) {
    const [_, prevIdx] = stocks.pop();

    answer[prevIdx] = length - prevIdx - 1;
  }
  return answer;
}
