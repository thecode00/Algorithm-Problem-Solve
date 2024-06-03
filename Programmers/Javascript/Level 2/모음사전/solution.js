// https://school.programmers.co.kr/learn/courses/30/lessons/84512?language=javascript

function solution(word) {
  const vowels = ["A", "E", "I", "O", "U"];

  function findWord(currentWord, count) {
    if (word === currentWord) {
      return [true, count];
    }

    if (currentWord.length === 5) {
      return [false, count];
    }

    for (let idx = 0; idx < 5; idx++) {
      count += 1;
      const [isFound, c] = findWord(currentWord + vowels[idx], count);
      count = c;
      if (isFound) {
        // 탐색 종료 플래그
        return [isFound, count];
      }
    }

    return [false, count];
  }
  return findWord("", 0)[1];
}
