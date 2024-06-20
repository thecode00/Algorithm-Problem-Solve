// https://school.programmers.co.kr/learn/courses/30/lessons/12971?language=javascript

function solution(sticker) {
	if (sticker.length === 1) {
		return sticker[0];
	}
	const dp1 = Array(sticker.length), // 첫번째를 무조건 뜯는경우
		dp2 = Array(sticker.length); // 첫번째를 무조건 안뜯는경우

	dp1[0] = sticker[0];
	dp1[1] = Math.max(sticker[0], sticker[1]);

	for (let idx = 2; idx < sticker.length - 1; idx++) {
		dp1[idx] = Math.max(dp1[idx - 1], dp1[idx - 2] + sticker[idx]);
	}

	dp2[0] = 0;
	dp2[1] = sticker[1];

	for (let idx = 2; idx < sticker.length; idx++) {
		if (idx < sticker.length - 1) {
			dp1[idx] = Math.max(dp1[idx - 1], dp1[idx - 2] + sticker[idx]);
		}

		dp2[idx] = Math.max(dp2[idx - 1], dp2[idx - 2] + sticker[idx]);
	}

	return Math.max(dp1.at(-2), dp2.at(-1));
}
