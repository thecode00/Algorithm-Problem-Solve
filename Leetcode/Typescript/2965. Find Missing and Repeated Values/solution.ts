// https://leetcode.com/problems/find-missing-and-repeated-values/description

function findMissingAndRepeatedValues(grid: number[][]): number[] {
  const count = Array.from({ length: grid.length ** 2 + 1 }, (_) => 0);

  for (let y = 0; y < grid.length; y++) {
    for (let x = 0; x < grid.length; x++) {
      count[grid[y][x]] += 1;
    }
  }

  const result = [0, 0];

  for (let num = 1; num < count.length; num++) {
    if (count[num] === 0) {
      result[1] = num;
    } else if (count[num] === 2) {
      result[0] = num;
    }
  }

  return result;
}
