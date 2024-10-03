// https://bigfrontend.dev/problem/implement-Object.is

/**
 * @param {any} a
 * @param {any} b
 * @return {boolean}
 */
function is(a, b) {
  // Check -0, 0
  if (a === 0 && b === 0) {
    return 1 / a === 1 / b;
  }
  // Check NaN
  if (a !== a) {
    return b !== b;
  }

  return a === b;
}
