// https://leetcode.com/problems/maximum-odd-binary-number/description/

/**
 * @param {string} s
 * @return {string}
 */
var maximumOddBinaryNumber = function (s) {
	// Convert to integer and count of 1-bit
	let countOneBits = 0,
		numberS = parseInt(parseInt(s, 10), 2);
	while (numberS > 0) {
		countOneBits += numberS & 1;
		numberS >>= 1;
	}
	countOneBits -= 1;
	return (
		"1".repeat(countOneBits) + "0".repeat(s.length - countOneBits - 1) + "1"
	);
};
