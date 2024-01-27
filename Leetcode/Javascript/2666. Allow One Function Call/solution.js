/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function (fn) {
  let count = 0;
  // Closure: a function can remember the environment in which it was declared, regardless of where it is executed
  return function (...args) {
    if (count >= 1) {
      return;
    }
    count++;
    return fn(...args);
  };
};

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
