// https://leetcode.com/problems/three-consecutive-odds/description

function threeConsecutiveOdds(arr: number[]): boolean {
  for (let idx = 0; idx < arr.length - 2; idx++) {
    let isOdd = true;

    for (let i = idx; i < idx + 3; i++) {
      if (arr[i] % 2 === 0) {
        isOdd = false;
        break;
      }
    }

    if (isOdd) {
      return true;
    }
  }

  return false;
}
