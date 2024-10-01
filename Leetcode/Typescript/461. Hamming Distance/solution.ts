// https://leetcode.com/problems/hamming-distance/description/

function hammingDistance(x: number, y: number): number {
  let num = x ^ y;
  let count = 0;

  while (num > 0) {
    count += 1;
    num &= num - 1;
  }
  return count;
}
