// https://school.programmers.co.kr/learn/courses/30/lessons/132265?language=javascript

class Counter {
  constructor() {
    this.counter = new Map();
  }

  count(key) {
    if (!this.isInclude(key)) {
      this.counter.set(key, 0);
    }

    this.counter.set(key, this.counter.get(key) + 1);
  }

  subtract(key) {
    const count = this.counter.get(key);

    if (count === 1) {
      this.counter.delete(key);
    } else {
      this.counter.set(key, count - 1);
    }
  }

  isInclude(key) {
    return this.counter.has(key);
  }

  size() {
    return this.counter.size;
  }
}

function solution(topping) {
  const chulTopping = new Counter(),
    brotherTopping = new Counter();
  let answer = 0;

  // 처음엔 모든 토핑을 철수에게
  for (const t of topping) {
    chulTopping.count(t);
  }

  for (const t of topping) {
    chulTopping.subtract(t);
    brotherTopping.count(t);

    if (chulTopping.size() === brotherTopping.size()) {
      answer += 1;
    } else if (chulTopping.size() < brotherTopping.size()) {
      // 철수의 토핑은 계속 빼므로 동생의 토핑 종류보다 적으면 탐색 종료
      break;
    }
  }

  return answer;
}
