// https://leetcode.com/problems/assign-cookies/description/

function findContentChildren(g: number[], s: number[]): number {
  g.sort((a, b) => a - b);
  s.sort((a, b) => a - b);
  let pointG = 0;
  let assign = 0;

  for (let idx = 0; idx < s.length; idx++) {
    if (pointG === g.length) {
      break;
    }

    if (s[idx] >= g[pointG]) {
      assign += 1;
      pointG += 1;
    }
  }

  return assign;
}
