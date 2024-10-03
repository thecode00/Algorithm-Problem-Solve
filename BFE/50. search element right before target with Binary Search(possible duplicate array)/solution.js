// https://bigfrontend.dev/problem/search-element-right-before-target-with-Binary-Search-possible-duplicate-array

/**
 * @param {number[]} arr - ascending array with duplicates
 * @param {number} target
 * @return {number}
 */
function elementBefore(arr, target) {
  let left = 0,
    right = arr.length - 1;

  while (left <= right) {
    const mid = left + Math.floor((right - left) / 2);

    if (arr[mid] >= target) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
  }

  return arr[left] === target ? arr[right] : undefined;
}
