/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
  let result = [];
  for (let element of arr) {
    temp.push(element);
    if (Array.isArray(element)) {
      result.push(temp);
      temp = [];
    }
  }
  return result;
};
