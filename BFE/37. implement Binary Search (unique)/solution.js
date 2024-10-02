// https://bigfrontend.dev/problem/implement-Binary-Search-Unique

/**
 * @param {number[]} arr - ascending unique array
 * @param {number} target
 * @return {number}
 */
function binarySearch(arr, target) {
  let start = 0,
    end = arr.length - 1;

  while (start <= end) {
    const mid = start + Math.floor((end - start) / 2);

    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  return -1;
}
