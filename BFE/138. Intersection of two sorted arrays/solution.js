// https://bigfrontend.dev/problem/intersection-of-two0-sorted-Arrays

/**
 * @param {number[]} arr1 - integers
 * @param {number[]} arr2 - integers
 * @returns {number[]}
 */
function intersect(arr1, arr2) {
  const result = [];
  arr1.sort((a, b) => a - b);
  arr2.sort((a, b) => a - b);

  let idx1 = 0,
    idx2 = 0;

  while (idx1 < arr1.length && idx2 < arr2.length) {
    if (arr1[idx1] === arr2[idx2]) {
      result.push(arr1[idx1]);
      idx2 += 1;
    }
    idx1 += 1;
  }

  return result;
}
