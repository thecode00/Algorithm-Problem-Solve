// https://school.programmers.co.kr/learn/courses/30/lessons/68936?language=javascript

function solution(arr) {
  const answer = [0, 0];
  check(arr, 0, 0, arr.length, answer);
  return answer;
}

/**
 *
 * @param {} arr
 * @param {*} startX
 * @param {*} startY
 * @param {*} size
 * @param {*} answer
 * @returns
 */
function check(arr, startX, startY, size, answer) {
  const checkNumber = arr[startY][startX];

  for (let y = startY; y < startY + size; y++) {
    for (let x = startX; x < startX + size; x++) {
      if (arr[y][x] !== checkNumber) {
        const halfSize = size / 2;

        check(arr, startX, startY, halfSize, answer);
        check(arr, startX, startY + halfSize, halfSize, answer);
        check(arr, startX + halfSize, startY, halfSize, answer);
        check(arr, startX + halfSize, startY + halfSize, halfSize, answer);
        return;
      }
    }
  }

  answer[checkNumber] += 1;
}
