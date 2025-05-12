// https://leetcode.com/problems/finding-3-digit-even-numbers/description

function findEvenNumbers(digits: number[]): number[] {
  const count = Array(10).fill(0);

  for (const num of digits) {
    count[num] += 1;
  }

  const result: number[] = [];

  for (let target = 100; target < 1000; target += 2) {
    const first = Math.floor(target / 100);
    const second = Math.floor((target / 10) % 10);
    const third = target % 10;

    // Use digits to form the target number
    count[first] -= 1;
    count[second] -= 1;
    count[third] -= 1;

    if (count[first] >= 0 && count[second] >= 0 && count[third] >= 0) {
      result.push(target);
    }

    count[first] += 1;
    count[second] += 1;
    count[third] += 1;
  }

  return result;
}
