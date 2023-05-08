// https://leetcode.com/problems/counter-ii/

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function (init) {
	let changeNumber = init;
	return {
		increment: () => {
			return ++changeNumber;
		},
		decrement: () => {
			return --changeNumber;
		},
		reset: () => {
			changeNumber = init;
			return changeNumber;
		},
	};
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
