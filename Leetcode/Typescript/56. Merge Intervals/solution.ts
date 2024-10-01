// https://leetcode.com/problems/merge-intervals/description/

function merge(intervals: number[][]): number[][] {
  intervals.sort((a, b) => {
    return a[0] - b[0];
  });
  const stack: number[][] = [];

  for (const [start, end] of intervals) {
    if (stack.length === 0 || stack[stack.length - 1][1] < start) {
      stack.push([start, end]);
    } else {
      stack[stack.length - 1][1] = Math.max(stack[stack.length - 1][1], end);
    }
  }

  return stack;
}
