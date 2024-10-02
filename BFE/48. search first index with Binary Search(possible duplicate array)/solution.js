// https://bigfrontend.dev/problem/search-first-index-with-Binary-Search-duplicate-array

/**
 * @param {number[]} arr - ascending array with duplicates
 * @param {number} target
 * @return {number}
 */
function firstIndex(arr, target) {
  let left = 0,
    right = arr.length - 1;
  while (left < right) {
    const mid = left + Math.floor((right - left) / 2);

    if (arr[mid] >= target) {
      right = mid;
    } else {
      left = mid + 1;
    }
  }

  return arr[left] === target ? left : -1;
}
