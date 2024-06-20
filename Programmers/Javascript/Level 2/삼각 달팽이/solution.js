// https://school.programmers.co.kr/learn/courses/30/lessons/68645?language=javascript

function solution(n) {
  const triangle = [];
  for (let size = 1; size <= n; size++) {
    triangle.push(Array(size).fill(0));
  }

  let y = -1,
    x = 0,
    moveSize = n,
    turn = 0, // 0: 아래로 감, 1: 오른쪽으로 감: 2: 위로 감
    num = 1;

  while (moveSize > 0) {
    for (let i = 0; i < moveSize; i++) {
      if (turn === 0) {
        y += 1;
      } else if (turn === 1) {
        x += 1;
      } else {
        y -= 1;
        x -= 1;
      }

      triangle[y][x] = num;
      num += 1;
    }

    moveSize -= 1;
    turn = (turn + 1) % 3;
  }
  // 2차원 배열 평탄화
  return triangle.flat();
}
