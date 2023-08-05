// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  for (let idx = 0; idx < arr.length; idx++) {
    arr[idx] = fn(arr[idx], idx);
  }
  return arr;
};

var map = function (arr, fn) {
  arr.forEach((ele, idx) => {
    arr[idx] = fn(ele, idx);
  });
  return arr;
};
