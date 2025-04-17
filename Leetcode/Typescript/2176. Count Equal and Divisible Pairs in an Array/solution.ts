// https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description

function countPairs(nums: number[], k: number): number {
  const indexHash = new Map<number, number[]>();
  let pairs = 0;

  for (let idx = 0; idx < nums.length; idx++) {
    const key = nums[idx];
    if (!indexHash.has(key)) {
      indexHash.set(key, []);
    } else {
      for (const i of indexHash.get(key)!) {
        if ((idx * i) % k === 0) {
          pairs += 1;
        }
      }
    }

    indexHash.get(key)!.push(idx);
  }

  return pairs;
}
