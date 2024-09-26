// https://leetcode.com/problems/jewels-and-stones/description/

function numJewelsInStones(jewels: string, stones: string): number {
  const jewelSet = new Set<string>(jewels);
  let count = 0;

  for (const stone of stones) {
    if (jewelSet.has(stone)) {
      count += 1;
    }
  }

  return count;
}
