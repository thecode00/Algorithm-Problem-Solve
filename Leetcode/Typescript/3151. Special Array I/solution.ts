// https://leetcode.com/problems/special-array-i/description

function isArraySpecial(nums: number[]): boolean {
  for (let idx = 1; idx < nums.length; idx++) {
    if ((nums[idx - 1] & 1) === (nums[idx] & 1)) {
      return false;
    }
  }
  return true;
}
