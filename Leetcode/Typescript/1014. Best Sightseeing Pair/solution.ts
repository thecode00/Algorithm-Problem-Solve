// https://leetcode.com/problems/best-sightseeing-pair/description

function maxScoreSightseeingPair(values: number[]): number {
  let maxLeft = values[0];
  let maxValue = 0;
  // Maximize values[i] + i
  for (let idx = 1; idx < values.length; idx++) {
    maxValue = Math.max(maxValue, maxLeft + values[idx] - idx);
    maxLeft = Math.max(maxLeft, values[idx] + idx);
  }

  return maxValue;
}
