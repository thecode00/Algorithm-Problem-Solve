// https://bigfrontend.dev/problem/Find-the-largest-difference

/**
 * @param {number[]} arr
 * @return {number}
 */
function largestDiff(arr) {
  if (arr.length <= 1) {
    return 0;
  }

  arr.sort((a, b) => a - b);
  return Math.abs(arr[0] - arr[arr.length - 1]);
}
