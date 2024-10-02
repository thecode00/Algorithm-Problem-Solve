// https://bigfrontend.dev/problem/add-BigInt-string

/**
 * @param {string} num1
 * @param {string} num2
 * @return {string}
 */
function add(num1, num2) {
  let idx1 = num1.length - 1,
    idx2 = num2.length - 1;
  let carry = 0;
  const result = [];

  while (idx1 >= 0 || idx2 >= 0 || carry) {
    let total = carry;

    total += parseInt(num1[idx1--]) || 0;
    total += parseInt(num2[idx2--]) || 0;

    result.push(total % 10);
    carry = total >= 10 ? 1 : 0;
  }

  return result.reverse().join("");
}
