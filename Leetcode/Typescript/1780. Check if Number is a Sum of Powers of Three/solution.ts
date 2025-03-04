// https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/description

function checkPowersOfThree(n: number): boolean {
  const powerSet = new Set<number>();

  let power = 0;

  while (3 ** power <= n) {
    powerSet.add(3 ** power);
    power += 1;
  }

  const powerValue = Array.from(powerSet.values());
  powerValue.sort((a, b) => a - b);

  for (let idx = powerValue.length - 1; idx >= 0; idx--) {
    if (powerValue[idx] <= n) {
      n -= powerValue[idx];
      powerSet.delete(n);
    }
  }

  return n == 0;
}
