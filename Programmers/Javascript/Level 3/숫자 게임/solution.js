// https://school.programmers.co.kr/learn/courses/30/lessons/12987?language=javascript

function solution(A, B) {
  A.sort((a, b) => a - b);
  B.sort((a, b) => a - b);

  let answer = 0,
    remainCrew = 0;

  for (let idx = 0; idx < A.length; idx++) {
    if (remainCrew === B.length) {
      break;
    }
    // B에 남은 크루중 A의 크루를 이길수 있는 가장 작은 B크루를 찾음
    for (let crew = remainCrew; crew < B.length; crew++) {
      remainCrew += 1;
      if (B[crew] > A[answer]) {
        answer += 1;
        break;
      }
    }
  }
  return answer;
}
