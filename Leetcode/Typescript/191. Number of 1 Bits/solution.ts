// https://leetcode.com/problems/number-of-1-bits/description/

function hammingWeight(n: number): number {
  let count = 0;

  while (n > 0) {
    count += 1;
    n &= n - 1;
  }

  return count;
}
