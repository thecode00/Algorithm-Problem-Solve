// https://leetcode.com/problems/count-symmetric-integers/description

function countSymmetricIntegers(low: number, high: number): number {
  let count = 0;

  for (let n = low; n <= high; n++) {
    let num = n;
    const digits: number[] = [];

    while (num >= 10) {
      digits.push(num % 10);
      num = Math.floor(num / 10);
    }
    digits.push(num);

    if (digits.length % 2 === 0 && isSymmetric(digits)) {
      count += 1;
    }
  }

  return count;
}

function isSymmetric(digits: number[]): boolean {
  const mid = Math.floor(digits.length / 2);
  let left = 0;
  let right = 0;

  for (let idx = 0; idx < mid; idx++) {
    left += digits[idx];
    right += digits[mid + idx];
  }

  return left === right;
}
