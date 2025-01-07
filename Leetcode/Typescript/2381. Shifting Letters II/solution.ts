// https://leetcode.com/problems/shifting-letters-ii/description

function shiftingLetters(s: string, shifts: number[][]): string {
  const diffArray = Array.from({ length: s.length }, (_) => 0);

  for (const [start, end, direction] of shifts) {
    if (direction) {
      diffArray[start] += 1;
      if (end + 1 < s.length) {
        diffArray[end + 1] -= 1;
      }
    } else {
      diffArray[start] -= 1;
      if (end + 1 < s.length) {
        diffArray[end + 1] += 1;
      }
    }
  }

  let moveCount = 0;
  const result: string[] = [];
  const A_CODE = "a".charCodeAt(0);

  for (let idx = 0; idx < s.length; idx++) {
    moveCount += diffArray[idx] % 26;
    if (moveCount < 0) {
      moveCount += 26;
    }

    result.push(
      String.fromCharCode(
        ((s.charCodeAt(idx) - A_CODE + moveCount) % 26) + A_CODE
      )
    );
  }

  return result.join("");
}
