// https://leetcode.com/problems/number-of-islands/description/

interface point {
  x: number;
  y: number;
}

function numIslands(grid: string[][]): number {
  const stack: point[] = [];
  const dy = [0, 0, 1, -1],
    dx = [1, -1, 0, 0];
  const rowLength = grid.length,
    colLength = grid[0].length;
  let number = 0;

  for (let y = 0; y < rowLength; y++) {
    for (let x = 0; x < colLength; x++) {
      if (grid[y][x] === "1") {
        number += 1;
        stack.push({ x, y });

        while (stack.length > 0) {
          let cur = stack.pop();

          for (let i = 0; i < 4; i++) {
            const newX = cur!.x + dx[i],
              newY = cur!.y + dy[i];

            if (
              0 <= newX &&
              newX < colLength &&
              0 <= newY &&
              newY < rowLength &&
              grid[newY][newX] === "1"
            ) {
              grid[newY][newX] = "0";
              stack.push({ x: newX, y: newY });
            }
          }
        }
      }
    }
  }

  return number;
}
