// https://leetcode.com/problems/permutations/description/

function permute(nums: number[]): number[][] {
  const result: number[][] = [];
  function dfs(prev: number[], usedIndex: Set<number>) {
    if (prev.length === nums.length) {
      result.push(prev.slice());
      return;
    }

    for (let idx = 0; idx < nums.length; idx++) {
      if (usedIndex.has(idx)) {
        continue;
      }

      prev.push(nums[idx]);
      usedIndex.add(idx);
      dfs(prev, usedIndex);
      usedIndex.delete(idx);
      prev.pop();
    }
  }
  dfs([], new Set());

  return result;
}
