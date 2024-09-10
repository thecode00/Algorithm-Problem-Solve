// https://leetcode.com/problems/combination-sum/description/

function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  function dfs(prev: number[], index: number, total: number) {
    if (total === target) {
      result.push(prev.slice());
      return;
    }

    for (let idx = index; idx < candidates.length; idx++) {
      total += candidates[idx];
      prev.push(candidates[idx]);
      // Backtracking
      if (total <= target) {
        dfs(prev, idx, total);
      }
      total -= candidates[idx];
      prev.pop();
    }
  }

  dfs([], 0, 0);

  return result;
}
