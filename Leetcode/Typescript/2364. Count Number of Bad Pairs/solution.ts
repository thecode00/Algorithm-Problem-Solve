// https://leetcode.com/problems/count-number-of-bad-pairs/description

function countBadPairs(nums: number[]): number {
  const pairNumberCount = new Map<number, number>();
  let badPairs = 0;

  for (let idx = 0; idx < nums.length; idx++) {
    // (j - i != nums[j] - nums[i]) can be (nums[i] - i != nums[j] - j)
    const pairNumber = nums[idx] - idx;
    badPairs += idx - (pairNumberCount.get(pairNumber) || 0);

    pairNumberCount.set(pairNumber, (pairNumberCount.get(pairNumber) || 0) + 1);
  }

  return badPairs;
}
