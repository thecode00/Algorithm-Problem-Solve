// https://bigfrontend.dev/problem/Find-two-numbers-that-sum-up-to-0

/**
 * @param {number[]} arr
 * @return {number[]}
 */
function findTwo(arr) {
  arr.sort((a, b) => a - b);

  let left = 0,
    right = arr.length - 1;
  while (left < right) {
    const twoSum = arr[left] + arr[right];

    if (twoSum > 0) {
      right -= 1;
    } else if (twoSum < 0) {
      left += 1;
    } else {
      return [left, right];
    }
  }

  return null;
}
