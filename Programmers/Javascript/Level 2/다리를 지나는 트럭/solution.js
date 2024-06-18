// https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=javascript

function solution(bridge_length, weight, truck_weights) {
  const bridgeQueue = new Queue();
  let currentTruck = 0, // 지나가야하는 트럭중 가장 앞에있는 트럭
    crossedTruck = 0, // 지나간 트럭의 개수
    currentBridgeWeight = 0, // 현재 브릿지의 무게
    time = 0;

  // 시간을 1초씩 늘리면서 트럭을 다리에 넣고 빼는 과정을 반복
  while (crossedTruck < truck_weights.length) {
    time += 1;
    // 다리위에 있는 가장 앞에있는 트럭이 나갈때가 되었는지 확인
    if (
      !bridgeQueue.isEmpty() &&
      time - bridgeQueue.getFront()[1] >= bridge_length
    ) {
      currentBridgeWeight -= bridgeQueue.deQueue()[0];
      crossedTruck += 1;
    }

    // 다리의 무게제한에 걸려서 트럭이 들어갈수없거나 남은 트럭이 없고 다리위에 트럭만 남아있는경우 시간만 보냄
    if (
      currentBridgeWeight + truck_weights[currentTruck] > weight ||
      currentTruck >= truck_weights.length
    ) {
      continue;
    }

    currentBridgeWeight += truck_weights[currentTruck];
    bridgeQueue.enQueue([truck_weights[currentTruck], time]);
    currentTruck += 1;
  }
  return time;
}

class Queue {
  constructor() {
    this.queue = {};
    this.size = 0;
    this.front = 0;
    this.back = -1;
  }

  isEmpty() {
    return this.size === 0;
  }

  enQueue(value) {
    this.back += 1;
    this.size += 1;
    this.queue[this.back] = value;
  }

  deQueue() {
    if (this.isEmpty()) {
      throw new Error("Empty queue!");
    }
    this.size -= 1;
    const returnValue = this.queue[this.front];
    delete this.queue[this.front];
    this.front += 1;
    return returnValue;
  }

  getFront() {
    if (this.isEmpty()) {
      throw new Error("Empty queue!");
    }
    return this.queue[this.front];
  }
}
