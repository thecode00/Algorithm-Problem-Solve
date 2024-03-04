// https://leetcode.com/problems/squares-of-a-sorted-array/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
	for (let idx = 0; idx < nums.length; idx++) {
		nums[idx] **= 2;
	}
	nums.sort((a, b) => a - b);
	return nums;
};
