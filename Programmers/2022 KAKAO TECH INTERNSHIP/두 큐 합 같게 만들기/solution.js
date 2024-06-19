// https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=javascript

function solution(queue1, queue2) {
  const newQueue1 = new Queue(),
    newQueue2 = new Queue();

  for (let idx = 0; idx < queue1.length; idx++) {
    newQueue1.push(queue1[idx]);
    newQueue2.push(queue2[idx]);
  }

  let count = 0;

  // queue1.length * 3만큼 원소를 움직이면 queue1에 있는 원소를 다 비우고 queue2에 있는 원소를 다시 queue1에 옮겨도
  // 같게 만들수 없는경우지만 넉넉하게 4를 곱함
  for (let moveCount = 0; moveCount < queue1.length * 4; moveCount++) {
    if (newQueue1.getTotal() === newQueue2.getTotal()) {
      break;
    }

    count += 1;

    if (newQueue1.getTotal() > newQueue2.getTotal()) {
      newQueue2.push(newQueue1.pop());
    } else {
      newQueue1.push(newQueue2.pop());
    }
  }

  return newQueue1.getTotal() === newQueue2.getTotal() ? count : -1;
}

class Queue {
  constructor() {
    this._queue = {};
    this._front = 0;
    this._back = -1;
    this._size = 0;
    this._total = 0;
  }

  isEmpty() {
    return this._size === 0;
  }

  push(value) {
    this._size += 1;
    this._total += value;
    this._back += 1;
    this._queue[this._back] = value;
  }

  pop() {
    if (this.isEmpty()) {
      throw new Error("Popped empty queue!");
    }

    this._size -= 1;
    const returnValue = this._queue[this._front];
    this._total -= returnValue;
    delete this._queue[this._front];
    this._front += 1;

    return returnValue;
  }

  getTotal() {
    return this._total;
  }
}
