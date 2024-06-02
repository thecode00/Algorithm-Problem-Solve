// https://www.greatfrontend.com/questions/javascript/stack

export default class Stack<T> {
  private size = 0;
  private index = 0;
  private stack = {};

  /**
   * Pushes an item onto the top of the stack.
   */
  push(item: T): number {
    if (!this.isEmpty()) {
      this.index += 1;
    }
    this.size += 1;
    this.stack[this.index] = item;

    return this.size;
  }

  /**
   * Remove an item at the top of the stack.
   */
  pop(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }
    this.size -= 1;
    return this.stack[this.index--];
  }

  /**
   * Determines if the stack is empty.
   */
  isEmpty(): boolean {
    return this.size <= 0;
  }

  /**
   * Returns the item at the top of the stack without removing it from the stack.
   */
  peek(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    return this.stack[this.index];
  }

  /**
   * Returns the number of items in the stack.
   */
  length(): number {
    return this.size;
  }
}
