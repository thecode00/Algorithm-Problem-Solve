// https://bigfrontend.dev/problem/isPrime

/**
 * @param {number} num - positive integer
 */
function isPrime(num) {
  if (num <= 1) {
    return false;
  }

  for (let n = 2; n <= Math.floor(Math.sqrt(num)); n++) {
    if (num % n === 0) {
      return false;
    }
  }

  return true;
}
