// https://school.programmers.co.kr/learn/courses/30/lessons/43163?language=javascript

class Queue {
  // 자바스크립트에는 내장된 큐가 없어서 직접 구현
  constructor() {
    this.queue = {};
    this.size = 0;
    this.end = 0;
    this.start = 0;
  }

  push(val) {
    this.size += 1;
    this.queue[this.end++] = val;
  }

  pop() {
    if (this.isEmpty()) {
      throw new Error("Pop empty queue!");
    }

    this.size -= 1;
    const returnValue = this.queue[this.start];
    delete this.queue[this.start];
    this.start += 1;
    return returnValue;
  }

  isEmpty() {
    return this.size <= 0;
  }
}

function solution(begin, target, words) {
  if (!words.includes(target)) {
    return 0;
  }
  const queue = new Queue();

  queue.push([begin, 0]);
  while (!queue.isEmpty()) {
    const [currentWord, count] = queue.pop();

    if (currentWord === target) {
      return count;
    }

    if (count === length) {
      // 사이클이 생긴 경우이므로 무시
      continue;
    }

    for (const word of words) {
      let diff = 0;

      for (let idx = 0; idx < word.length; idx++) {
        if (currentWord[idx] !== word[idx]) {
          diff += 1;
        }
      }

      if (diff === 1) {
        queue.push([word, count + 1]);
      }
    }
  }

  return 0;
}
