// https://leetcode.com/problems/sliding-window-maximum/description/

function maxSlidingWindow(nums: number[], k: number): number[] {
  const stack: number[] = [];
  const result: number[] = [];

  for (let idx = 0; idx < nums.length; idx++) {
    while (stack.length > 0 && nums[stack[stack.length - 1]] < nums[idx]) {
      stack.pop();
    }
    stack.push(idx);

    if (stack[0] === idx - k) {
      stack.shift();
    }

    if (idx >= k - 1) {
      result.push(nums[stack[0]]);
    }
  }
  return result;
}
