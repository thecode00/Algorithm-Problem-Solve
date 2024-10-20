// https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/description

function findKthBit(n: number, k: number): string {
  if (n <= 1) {
    return "0";
  }
  // BitsSize is twice previous bits + 1
  const bitsSize = (1 << n) - 1;
  // k is 1-index so add 1
  const half = Math.floor(bitsSize / 2) + 1;

  // k in left half
  if (k < half) {
    return findKthBit(n - 1, k);
  } else if (k === half) {
    return "1";
  } else {
    // k in right half
    const targetBit = findKthBit(n - 1, bitsSize - k + 1);

    return targetBit === "1" ? "0" : "1";
  }
}
