// https://leetcode.com/problems/array-reduce-transformation/

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function (nums, fn, init) {
	for (let idx = 0; idx < nums.length; idx++) {
		init = fn(init, nums[idx]);
	}
	return init;
};
