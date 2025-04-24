// https://leetcode.com/problems/count-largest-group/description

function countLargestGroup(n: number): number {
  const digitSumHash = new Map<number, number>();
  let maxGroup = 0;

  for (let num = 1; num <= n; num++) {
    const digitSum = getDigitSum(num);

    digitSumHash.set(digitSum, (digitSumHash.get(digitSum) || 0) + 1);
    maxGroup = Math.max(maxGroup, digitSumHash.get(digitSum)!);
  }

  // Find largest group size
  return Array.from(digitSumHash.values()).reduce((acc, cur) => {
    return cur === maxGroup ? acc + 1 : acc;
  }, 0);
}

function getDigitSum(n: number): number {
  let total = 0;

  while (n > 0) {
    total += n % 10;
    n = Math.floor(n / 10);
  }

  return total;
}
