// https://leetcode.com/problems/number-of-closed-islands/description/

function closedIsland(grid: number[][]): number {
  let closed = 0;

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid[0].length; x++) {
      if (grid[y][x] === 0) {
        closed += checkClosed(grid, x, y);
      }
    }
  }

  return closed;
}

function checkClosed(grid: number[][], x: number, y: number): number {
  const stack: number[][] = [[x, y]];
  const dx = [0, 0, 1, -1],
    dy = [1, -1, 0, 0];
  let isClosed = true;

  while (stack.length > 0) {
    const [cur_x, cur_y] = stack.pop();

    for (let i = 0; i < 4; i++) {
      const new_x = cur_x + dx[i],
        new_y = cur_y + dy[i];
      if (
        new_x < 0 ||
        grid[0].length <= new_x ||
        new_y < 0 ||
        grid.length <= new_y
      ) {
        isClosed = false;
        continue;
      }
      if (grid[new_y][new_x] === 0) {
        stack.push([new_x, new_y]);
        grid[new_y][new_x] = 1;
      }
    }
  }

  return isClosed ? 1 : 0;
}
