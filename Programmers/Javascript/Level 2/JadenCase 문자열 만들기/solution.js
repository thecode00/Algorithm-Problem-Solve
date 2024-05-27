// https://school.programmers.co.kr/learn/courses/30/lessons/12951?language=javascript#

function solution(s) {
  s = [...s];
  let isWord = false; // 현재 단어 첫글자인지 확인하는 bool

  for (let idx = 0; idx < s.length; idx++) {
    if (s[idx] === " ") {
      isWord = false;
    } else {
      if (!isWord) {
        isWord = true;
        s[idx] = s[idx].toUpperCase();
      } else {
        s[idx] = s[idx].toLowerCase();
      }
    }
  }

  return s.join("");
}
