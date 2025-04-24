// https://leetcode.com/problems/unique-paths/description/

function uniquePaths(m: number, n: number): number {
  // It can be space complexity: O(n)
  const grid = Array.from(Array(m), () => Array(n).fill(0));

  for (let col = 0; col < n; col++) {
    grid[0][col] = 1;
  }

  for (let row = 0; row < m; row++) {
    grid[row][0] = 1;
  }

  for (let row = 1; row < m; row++) {
    for (let col = 1; col < n; col++) {
      grid[row][col] = grid[row - 1][col] + grid[row][col - 1];
    }
  }

  return grid[m - 1][n - 1];
}
