// https://bigfrontend.dev/problem/compress-a-string

/**
 * @param {string} str
 * @return {string}
 */
function compress(str) {
  let idx = 0;
  const result = [];

  while (idx < str.length) {
    const cur = str[idx];
    let count = 0;

    while (idx < str.length && str[idx] === cur) {
      count += 1;
      idx += 1;
    }

    result.push(`${cur}${count > 1 ? count : ""}`);
  }

  return result.join("");
}
