// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/

function findNumbers(nums: number[]): number {
  let count = 0;

  for (const num of nums) {
    if (getNumberOfDigit(num) % 2 === 0) {
      count += 1;
    }
  }

  return count;
}

function getNumberOfDigit(num: number): number {
  let digitCount = 1;

  while (10 <= num) {
    digitCount += 1;
    num = Math.floor(num / 10);
  }

  return digitCount;
}
function findNumbers(nums: number[]): number {
  let count = 0;

  for (let num of nums) {
    let digits = 0;

    while (num > 0) {
      digits++;
      // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Bitwise_NOT
      // ~~(NOT NOT) is not a recommended method to truncate numbers to integers.
      //   num /= 10;
      //   num = ~~num;
      num = Math.trunc(num / 10);
    }

    if (digits % 2 == 0) {
      count++;
    }
  }

  return count;
}
