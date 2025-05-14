// https://leetcode.com/problems/total-characters-in-string-after-transformations-i/description

function lengthAfterTransformations(s: string, t: number): number {
  const MOD = 1_000_000_007;
  const queue: number[] = new Array(26).fill(0);

  for (const char of s) {
    const idx = char.charCodeAt(0) - "a".charCodeAt(0);
    queue[idx]++;
  }

  for (let step = 0; step < t; step++) {
    const z = queue[25] % MOD;
    for (let i = 25; i > 0; i--) {
      queue[i] = queue[i - 1];
    }
    queue[0] = z;
    queue[1] = (queue[1] + z) % MOD;
  }

  return queue.reduce((acc, val) => (acc + val) % MOD, 0);
}
