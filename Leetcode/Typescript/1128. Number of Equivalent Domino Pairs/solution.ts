// https://leetcode.com/problems/number-of-equivalent-domino-pairs/description

function numEquivDominoPairs(dominoes: number[][]): number {
  const hash = new Map<string, number>();
  let count = 0;

  for (const [a, b] of dominoes) {
    const key1 = `${a}${b}`;
    const key2 = `${b}${a}`;

    count += hash.get(key1) || 0;

    // Prevent duplicate
    if (a !== b) {
      count += hash.get(key2) || 0;
    }

    hash.set(key1, (hash.get(key1) || 0) + 1);
  }

  return count;
}
