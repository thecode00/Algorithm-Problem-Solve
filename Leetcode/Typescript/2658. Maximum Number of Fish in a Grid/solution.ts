// https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description

function findMaxFish(grid: number[][]): number {
  const dx = [0, 0, 1, -1];
  const dy = [1, -1, 0, 0];
  let maxFish = 0;

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[0].length; x++) {
      if (grid[y][x] !== 0) {
        let totalFish = 0;
        const stack: number[][] = [];
        stack.push([x, y]);

        while (stack.length) {
          const [curX, curY] = stack.pop();

          totalFish += grid[curY][curX];
          grid[curY][curX] = 0;

          for (let idx = 0; idx < 4; idx++) {
            const nextX = curX + dx[idx],
              nextY = curY + dy[idx];

            if (
              0 <= nextX &&
              nextX < grid[0].length &&
              0 <= nextY &&
              nextY < grid.length &&
              grid[nextY][nextX] !== 0
            ) {
              stack.push([nextX, nextY]);
            }
          }
        }

        maxFish = Math.max(maxFish, totalFish);
      }
    }
  }

  return maxFish;
}
