// https://bigfrontend.dev/problem/Implement-a-Stack-by-using-Queue

/* you can use this Queue which is bundled together with your code
class Queue {
  enqueue(element) {
    // add new element to the queue
  }
  peek() { 
    // return the head element
  }
  dequeue() { 
    // remove head element from the queue
  }
  size() { 
    // return the queue size
  }
}
*/

// you need to complete the following Stack, using only Queue
class Stack {
  constructor() {
    this.queue = new Queue();
  }

  push(element) {
    const popCount = this.size();
    this.queue.enqueue(element);
    for (let i = 0; i < popCount; i++) {
      this.queue.enqueue(this.queue.dequeue());
    }
  }
  peek() {
    return this.queue.peek();
  }
  pop() {
    return this.queue.dequeue();
  }
  size() {
    return this.queue.size();
  }
}
