// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description

function findThePrefixCommonArray(A: number[], B: number[]): number[] {
  const union = new Set<number>();
  const result: number[] = [];

  for (let idx = 0; idx < A.length; idx++) {
    union.add(A[idx]);
    union.add(B[idx]);

    // 2 * (idx + 1) = amount of prefix array element
    // intersection count = amount of prefix array element - len(union)
    result.push(2 * (idx + 1) - union.size);
  }

  return result;
}
