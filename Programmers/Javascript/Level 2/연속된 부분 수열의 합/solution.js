// https://school.programmers.co.kr/learn/courses/30/lessons/178870?language=javascript

function solution(sequence, k) {
	const answer = [0, 0];
	let left = 0,
		total = 0,
		minSize = Infinity;

	// right이 끝인 수열중 합이 k인 가장짧은 수열을 구함
	for (let right = 0; right < sequence.length; right++) {
		total += sequence[right];

		while (total > k && left <= right) {
			total -= sequence[left];
			left += 1;
		}
		// 이전보다 짧은 수열일때만 갱신
		if (total === k && right - left < minSize) {
			answer[0] = left;
			answer[1] = right;
			minSize = right - left;
		}
	}
	return answer;
}
