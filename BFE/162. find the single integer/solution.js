// https://bigfrontend.dev/problem/find-the-single-integer

/**
 * @param {number[]} arr
 * @returns number
 */
function findSingle(arr) {
  let number = 0;

  for (const num of arr) {
    number ^= num;
  }

  return number;
}
