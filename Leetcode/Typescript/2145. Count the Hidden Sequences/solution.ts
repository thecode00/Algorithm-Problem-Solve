// https://leetcode.com/problems/count-the-hidden-sequences/description

function numberOfArrays(
  differences: number[],
  lower: number,
  upper: number
): number {
  let prefixSum = 0;
  let minNum = 0;
  let maxNum = 0;

  // Compute prefix sums and track the min and max values
  for (const diff of differences) {
    prefixSum += diff;

    minNum = Math.min(minNum, prefixSum);
    maxNum = Math.max(maxNum, prefixSum);
  }

  const minStart = lower - minNum;
  const maxStart = upper - maxNum;

  // Calculate how many valid starting values arr[0] can take
  // so that all elements stay within [lower, upper]
  const count = maxStart - minStart + 1;

  // If the count is negative, it means no valid sequence exists
  return count < 0 ? 0 : count;
}
