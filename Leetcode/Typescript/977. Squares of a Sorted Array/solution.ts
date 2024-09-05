// https://leetcode.com/problems/squares-of-a-sorted-array/description/

function sortedSquares(nums: number[]): number[] {
  return nums
    .map((item) => {
      return item * item;
    })
    .sort((a, b) => {
      return a - b;
    });
}
