// https://leetcode.com/problems/separate-black-and-white-balls/description

function minimumSteps(s: string): number {
  let swapCount = 0,
    zeros = 0;

  for (let idx = 0; idx < s.length; idx++) {
    if (s[idx] === "0") {
      // We can swap only adjacent element, so swap step is (current index - (last zero index + 1))
      swapCount += idx - zeros;
      zeros += 1;
    }
  }

  return swapCount;
}
