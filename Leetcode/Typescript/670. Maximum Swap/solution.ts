// https://leetcode.com/problems/maximum-swap/description

function maximumSwap(num: number): number {
  const result = num.toString().split("").map(Number);
  const numLength = result.length;

  const maxIndex = Array(numLength);
  maxIndex[numLength - 1] = numLength - 1;

  for (let idx = numLength - 2; idx >= 0; idx--) {
    // Need to swap with the rightmost number that is greater than your current number,
    // so if the numbers are equal, you should record the index of the number on the right
    // If num = 3444, max_idx will be [3, 3, 3, 3]
    if (result[idx] <= result[maxIndex[idx + 1]]) {
      maxIndex[idx] = maxIndex[idx + 1];
    } else {
      maxIndex[idx] = idx;
    }
  }

  for (let idx = 0; idx < numLength; idx++) {
    if (result[idx] < result[maxIndex[idx]]) {
      [result[idx], result[maxIndex[idx]]] = [
        result[maxIndex[idx]],
        result[idx],
      ];
      break;
    }
  }

  return parseInt(result.join(""));
}
