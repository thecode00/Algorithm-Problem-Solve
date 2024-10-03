// https://bigfrontend.dev/problem/validate-parenthesis

/**
 * @param {string} str
 * @return {boolean}
 */
function validate(str) {
  const parenthesis = {
    "}": "{",
    ")": "(",
    "]": "[",
  };
  const stack = [];

  for (const char of str) {
    if (parenthesis[char]) {
      if (stack.length === 0 || stack[stack.length - 1] !== parenthesis[char]) {
        return false;
      }
      stack.pop();
    } else {
      stack.push(char);
    }
  }

  return stack.length === 0;
}
