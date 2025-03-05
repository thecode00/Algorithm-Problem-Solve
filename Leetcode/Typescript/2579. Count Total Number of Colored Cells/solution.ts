// https://leetcode.com/problems/count-total-number-of-colored-cells/description

function coloredCells(n: number): number {
  const blankCorner = ((n - 1) * n) / 2;
  return (2 * n - 1) ** 2 - 4 * blankCorner;
}
