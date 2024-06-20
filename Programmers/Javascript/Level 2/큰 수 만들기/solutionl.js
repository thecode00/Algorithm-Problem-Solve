// https://school.programmers.co.kr/learn/courses/30/lessons/42883?language=javascript

// 아이디어: 스택으로 local max를 찾으면서 숫자를 삭제
function solution(number, k) {
	const stack = [];
	let deleteCount = 0;

	for (const num of number) {
		while (stack.length > 0 && stack.at(-1) < num && deleteCount < k) {
			stack.pop();
			deleteCount += 1;
		}
		stack.push(num);
	}

	// 삭제해야하는 숫자들이 남은 경우 처리
	while (deleteCount < k) {
		stack.pop();
		deleteCount += 1;
	}
	return stack.join("");
}
