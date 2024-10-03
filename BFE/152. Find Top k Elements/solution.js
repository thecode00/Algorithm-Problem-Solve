// https://bigfrontend.dev/problem/top-k-elements

/*
 * @param {number[]} arr
 * @param {number} k
 * @returns {number[]}
 */
function topK(arr, k) {
  arr.sort((a, b) => a - b);

  return arr.slice(arr.length - k, arr.length).sort((a, b) => b - a);
}
