// https://leetcode.com/problems/product-of-the-last-k-numbers/description

class ProductOfNumbers {
  cache: number[] = [1];
  size = 0;

  constructor() {}

  add(num: number): void {
    if (num === 0) {
      this.size = 0;
      this.cache = [1];
    } else {
      this.cache.push(this.cache[this.size] * num);
      this.size += 1;
    }
  }

  getProduct(k: number): number {
    /**
     * We can assume that always the current list has at least k numbers
     *when add 0 we clear cache, so k > this.size is search product 0
     */
    if (k > this.size) {
      return 0;
    }

    return this.cache[this.size] / this.cache[this.size - k];
  }
}

/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * var obj = new ProductOfNumbers()
 * obj.add(num)
 * var param_2 = obj.getProduct(k)
 */
