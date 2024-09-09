// https://leetcode.com/problems/combinations/description/

function combine(n: number, k: number): number[][] {
  const result: number[][] = [];

  function dfs(prev: number[], index: number) {
    if (prev.length === k) {
      result.push(prev.slice());
      return;
    }

    for (let idx = index; idx <= n; idx++) {
      prev.push(idx);
      dfs(prev, idx + 1);
      prev.pop();
    }
  }

  dfs([], 1);

  return result;
}
