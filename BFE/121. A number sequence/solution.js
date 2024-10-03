// https://bigfrontend.dev/problem/A-number-sequence

/**
 * @param {number} n - integer
 * @returns {string}
 */
function getNthNum(n) {
  if (n <= 0) {
    return "";
  }

  let result = ["1"];

  while (n > 1) {
    const temp = [];
    let curChar = result[0],
      count = 0;

    for (const char of result) {
      if (char === curChar) {
        count += 1;
      } else {
        temp.push(count.toString());
        temp.push(curChar);

        curChar = char;
        count = 1;
      }
    }

    if (count > 0) {
      temp.push(count.toString());
      temp.push(curChar);
    }
    result = temp;
    n -= 1;
  }

  return result.join("");
}
