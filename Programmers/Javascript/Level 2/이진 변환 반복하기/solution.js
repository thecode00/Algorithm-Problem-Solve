// https://school.programmers.co.kr/learn/courses/30/lessons/70129?language=javascript

function solution(s) {
  const answer = [0, 0];

  while (s.length > 1) {
    let zero = 0,
      one = 0;

    for (let idx = 0; idx < s.length; idx++) {
      if (s[idx] === "1") {
        one += 1;
      } else {
        zero += 1;
      }
    }

    s = (s.length - zero).toString(2);
    answer[1] += zero;
    answer[0] += 1;
  }
  return answer;
}

solution("110010101001");
