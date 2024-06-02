// https://www.greatfrontend.com/questions/javascript/queue

export default class Queue<T> {
  private size = 0;
  private queue = {};
  private start = 0;
  private end = -1;

  /**
   * Adds an item to the back of the queue.
   * @param {T} item The item to be pushed onto the queue.
   * @return {number} The new length of the queue.
   */
  enqueue(item: T): number {
    this.end += 1;
    this.size += 1;
    this.queue[this.end] = item;
    console.log(this.queue);
    return this.size;
  }

  /**
   * Removes an item from the front of the queue.
   * @return {T | undefined} The item at the front of the queue if it is not empty, `undefined` otherwise.
   */
  dequeue(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    this.size -= 1;
    return this.queue[this.start++];
  }

  /**
   * Determines if the queue is empty.
   * @return {boolean} `true` if the queue has no items, `false` otherwise.
   */
  isEmpty(): boolean {
    return this.size <= 0;
  }

  /**
   * Returns the item at the front of the queue without removing it from the queue.
   * @return {T | undefined} The item at the front of the queue if it is not empty, `undefined` otherwise.
   */
  front(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    return this.queue[this.start];
  }

  /**
   * Returns the item at the back of the queue without removing it from the queue.
   * @return {T | undefined} The item at the back of the queue if it is not empty, `undefined` otherwise.
   */
  back(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    return this.queue[this.end];
  }

  /**
   * Returns the number of items in the queue.
   * @return {number} The number of items in the queue.
   */
  length(): number {
    return this.size;
  }
}
