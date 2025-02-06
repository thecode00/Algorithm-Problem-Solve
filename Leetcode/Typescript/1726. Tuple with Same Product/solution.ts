// https://leetcode.com/problems/tuple-with-same-product/description

function tupleSameProduct(nums: number[]): number {
  const productPairCount = new Map<number, number>();

  for (let idx1 = 0; idx1 < nums.length; idx1++) {
    for (let idx2 = idx1 + 1; idx2 < nums.length; idx2++) {
      const product = nums[idx1] * nums[idx2];
      productPairCount.set(product, (productPairCount.get(product) || 0) + 1);
    }
  }

  let tupleCount = 0;
  for (const val of productPairCount.values()) {
    tupleCount += Math.floor(((val - 1) * val) / 2);
  }
  // one unique (a, b, c, d) makes 8 tuple
  return tupleCount * 8;
}
