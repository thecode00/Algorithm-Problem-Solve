// https://leetcode.com/problems/subsets/description/

function subsets(nums: number[]): number[][] {
  const result: number[][] = [];
  function dfs(prev: number[], index: number) {
    result.push(prev.slice());
    if (prev.length === nums.length) {
      return;
    }

    for (let idx = index; idx < nums.length; idx++) {
      prev.push(nums[idx]);
      dfs(prev, idx + 1);
      prev.pop();
    }
  }

  dfs([], 0);
  return result;
}
