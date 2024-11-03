// https://leetcode.com/problems/rotate-string/description

function rotateString(s: string, goal: string): boolean {
  if (s.length !== goal.length) {
    return false;
  }
  // If goal is rotated string s, goal in double s
  s += s;

  return s.includes(goal);
}
