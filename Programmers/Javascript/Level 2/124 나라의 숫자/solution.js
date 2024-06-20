// https://school.programmers.co.kr/learn/courses/30/lessons/12899?language=javascript

// 3진수 구하는 문제
function solution(n) {
	n -= 1;
	if (n < 3) {
		return "124"[n];
	}
	const q = Math.floor(n / 3),
		r = n % 3;
	return solution(q) + "124"[r];
}
