// https://leetcode.com/problems/sleep/

/**
 * @param {number} millis
 */
async function sleep(millis) {
	// After execute resolve sleep can run then()
	await new Promise((resolve) => {
		setTimeout(resolve, millis);
	});
}

/**
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
