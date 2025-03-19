// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description

function minimumRecolors(blocks: string, k: number): number {
  let minRecolor = k;
  let needRecolor = k;

  for (let idx = 0; idx < blocks.length; idx++) {
    if (blocks[idx] === "B") {
      needRecolor -= 1;
    }

    if (idx >= k) {
      if (blocks[idx - k] === "B") {
        needRecolor += 1;
      }
    }
    minRecolor = Math.min(minRecolor, needRecolor);
  }

  return minRecolor;
}
