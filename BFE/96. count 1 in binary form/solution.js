// https://bigfrontend.dev/problem/how-many-1s-in-binary

/**
 * @param {number} num - integer
 * @return {number} count of 1 bit
 */
function countOne(num) {
  let count = 0;
  while (num > 0) {
    count += 1;
    num &= num - 1;
  }

  return count;
}
