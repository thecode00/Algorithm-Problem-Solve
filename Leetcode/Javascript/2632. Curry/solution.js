// https://leetcode.com/problems/curry/
// Ref: https://leetcode.com/problems/curry/solutions/3522382/easy-solution-2632-curry-level-up-your-javascript-skills-day-10/?utm_campaign=PostD10&utm_medium=Post&utm_source=Post&gio_link_id=QRekxgjo&orderBy=most_votes

/**
 * @param {Function} fn
 * @return {Function}
 */
var curry = function (fn) {
	// Use rest parameter
	return function curried(...args) {
		// function.length = number of function parameter
		if (fn.length > args.length) {
			return function (...args2) {
				return curried(...args, ...args2);
			};
		}
		return fn(...args);
	};
};

/**
 * function sum(a, b) { return a + b; }
 * const csum = curry(sum);
 * csum(1)(2) // 3
 */
