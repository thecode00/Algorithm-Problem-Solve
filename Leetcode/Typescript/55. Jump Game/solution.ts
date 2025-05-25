// https://leetcode.com/problems/jump-game/description/

function canJump(nums: number[]): boolean {
  let maxReach = 0;

  for (let idx = 0; idx < nums.length; idx++) {
    maxReach = Math.max(maxReach, idx + nums[idx]);
    if (idx === maxReach) {
      break;
    }
  }

  return maxReach >= nums.length - 1;
}
