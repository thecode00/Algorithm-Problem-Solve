// https://leetcode.com/problems/filter-elements-from-array/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  const newArray = [];
  let index = 0;
  for (const num of arr) {
    if (fn(num, index)) {
      newArray.push(num);
    }
    index += 1;
  }
  return newArray;
};

var filter = function (arr, fn) {
  return arr.filter((ele, idx) => fn(ele, idx));
};
