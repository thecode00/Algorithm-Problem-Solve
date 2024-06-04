// https://school.programmers.co.kr/learn/courses/30/lessons/49994?language=javascript

/**
 * 해당 좌표가 보드안 좌표인지 알려줌
 * @param {number} x x좌표
 * @param {number} y y좌표
 * @return {boolean} 보드안의 좌표라면 true반환
 */
function validPoint(x, y) {
  return -5 <= x && x <= 5 && -5 <= y && y <= 5;
}

/**
 * 새로운 경로인지 확인하고 새로운 경로일시 기록
 * @param {number} x 출발 x좌표
 * @param {number} y 출발 y좌표
 * @param {number} newX 도착 x좌표
 * @param {number} newY 도착 y좌표
 * @return {boolean} 새로운 경로라면 true반환
 */
function isNewPath(x, y, newX, newY, prevPath) {
  const startPoint = `${x}, ${y}`;
  const endPoint = `${newX}, ${newY}`;

  if (!prevPath[startPoint]) {
    prevPath[startPoint] = new Set();
  }

  if (!prevPath[endPoint]) {
    prevPath[endPoint] = new Set();
  }

  if (prevPath[startPoint].has(endPoint)) {
    return false;
  }

  prevPath[startPoint].add(endPoint);
  prevPath[endPoint].add(startPoint);
  return true;
}

function solution(dirs) {
  const prevPath = {};
  let x = 0,
    y = 0,
    answer = 0;

  for (const command of dirs) {
    let newX = x,
      newY = y;
    switch (command) {
      case "U":
        newY += 1;
        break;
      case "L":
        newX -= 1;
        break;
      case "R":
        newX += 1;
        break;
      case "D":
        newY -= 1;
        break;
    }

    if (validPoint(newX, newY)) {
      if (isNewPath(x, y, newX, newY, prevPath)) {
        answer += 1;
      }
      x = newX;
      y = newY;
    }
  }
  return answer;
}
