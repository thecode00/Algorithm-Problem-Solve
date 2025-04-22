// https://leetcode.com/problems/score-of-a-string/description

function scoreOfString(s: string): number {
  let score = 0;

  for (let idx = 1; idx < s.length; idx++) {
    score += Math.abs(s[idx - 1].charCodeAt(0) - s[idx].charCodeAt(0));
  }
  return score;
}
