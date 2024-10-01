// https://leetcode.com/problems/design-a-stack-with-increment-operation/description

class CustomStack {
  stack: number[] = [];
  maxSize: number;
  constructor(maxSize: number) {
    this.maxSize = maxSize;
  }

  push(x: number): void {
    if (this.maxSize !== this.stack.length) {
      this.stack.push(x);
    }
    console.log(this.stack);
  }

  pop(): number {
    if (this.stack.length === 0) {
      return -1;
    }

    return this.stack.pop() as number;
  }

  increment(k: number, val: number): void {
    let idx = 0;
    while (idx < this.stack.length && idx < k) {
      this.stack[idx] += val;
      idx += 1;
    }
  }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * var obj = new CustomStack(maxSize)
 * obj.push(x)
 * var param_2 = obj.pop()
 * obj.increment(k,val)
 */
