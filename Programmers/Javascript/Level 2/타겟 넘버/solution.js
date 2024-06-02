// https://school.programmers.co.kr/learn/courses/30/lessons/43165?language=javascript

class Queue {
  // 자바스크립트에는 큐가 내장되어있지않기에 새로 구현
  constructor() {
    this.queue = {};
    this.start = 0;
    this.end = -1;
    this.size = 0;
  }

  push(value) {
    this.end += 1;
    this.queue[this.end] = value;
    this.size += 1;
  }

  pop() {
    if (this.size === 0) {
      throw new Error("Empty queue!");
    }
    this.size -= 1;
    return this.queue[this.start++];
  }
}

function solution(numbers, target) {
  let answer = 0;
  const queue = new Queue();

  // 처음 숫자가 음수인 경우와 양수인 경우로 BFS탐색
  // [현재 숫자, 다음 숫자를 탐색할 인덱스]를 큐에 저장
  queue.push([-numbers[0], 1]);
  queue.push([numbers[0], 1]);

  while (queue.size > 0) {
    const [curNum, nextIndex] = queue.pop();
    if (nextIndex === numbers.length) {
      if (curNum === target) {
        answer += 1;
      }
      continue;
    }

    let sign = 1;
    for (let idx = 0; idx < 2; idx++) {
      queue.push([curNum + sign * numbers[nextIndex], nextIndex + 1]);
      sign *= -1;
    }
  }
  return answer;
}
