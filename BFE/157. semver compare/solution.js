// https://bigfrontend.dev/problem/semver-compare

/**
 * @param {string} v1
 * @param {string} v2
 * @returns 0 | 1 | -1
 */
function compare(v1, v2) {
  const l1 = v1.split("."),
    l2 = v2.split(".");

  for (let idx = 0; idx < l1.length; idx++) {
    const num1 = Number(l1[idx]),
      num2 = Number(l2[idx]);
    if (num1 > num2) {
      return 1;
    } else if (num1 < num2) {
      return -1;
    }
  }

  return 0;
}
