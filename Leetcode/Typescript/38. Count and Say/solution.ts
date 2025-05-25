// https://leetcode.com/problems/count-and-say/

function countAndSay(n: number): string {
  let result: string[] = ["1"];

  while (n > 1) {
    const temp: string[] = [];
    let cur = result[0];
    let count = 0;

    for (const char of result) {
      if (cur === char) {
        count += 1;
      } else {
        temp.push(count.toString());
        temp.push(cur);
        count = 1;
        cur = char;
      }
    }
    if (count !== 0) {
      temp.push(count.toString());
      temp.push(cur);
    }

    result = temp;
    n -= 1;
  }

  return result.join("");
}
