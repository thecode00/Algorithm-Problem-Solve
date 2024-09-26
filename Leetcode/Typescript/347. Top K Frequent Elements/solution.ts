// https://leetcode.com/problems/top-k-frequent-elements/description/

function topKFrequent(nums: number[], k: number): number[] {
  const counter = new Map<number, number>();

  for (const num of nums) {
    if (!counter.has(num)) {
      counter.set(num, 0);
    }
    counter.set(num, counter.get(num)! + 1);
  }

  const mostCommon = Array.from(counter.entries());
  mostCommon.sort((a, b) => {
    return b[1] - a[1];
  });

  const result: number[] = [];
  for (let i = 0; i < k; i++) {
    result.push(mostCommon[i][0]);
  }

  return result;
}
