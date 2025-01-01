// https://leetcode.com/problems/maximum-score-after-splitting-a-string/description

function maxScore(s: string): number {
  let one = 0;
  let zero = 0;
  let maxScore = Number.MIN_SAFE_INTEGER;

  // score = leftZero + rightOne = leftZero + totalOne - leftOne
  // We need maximize leftZero - leftOne
  for (let idx = 0; idx < s.length - 1; idx++) {
    if (s[idx] === "0") {
      zero += 1;
    } else {
      one += 1;
    }
    maxScore = Math.max(maxScore, zero - one);
  }

  if (s[s.length - 1] === "1") {
    one += 1;
  }
  //   Add totalOne
  return maxScore + one;
}

function maxScore(s: string): number {
  let one = 0;

  for (let num of s) {
    one += parseInt(num);
  }

  let zero = 0;
  let maxScore = 0;
  for (let idx = 0; idx < s.length - 1; idx++) {
    if (parseInt(s[idx]) === 0) {
      zero += 1;
    } else {
      one -= 1;
    }
    maxScore = Math.max(maxScore, zero + one);
  }
  return maxScore;
}
