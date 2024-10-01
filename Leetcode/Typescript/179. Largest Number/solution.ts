// https://leetcode.com/problems/largest-number/description/

function largestNumber(nums: number[]): string {
  nums.sort((a, b) => {
    const strA = a.toString(),
      strB = b.toString();

    return parseInt(strB + strA) - parseInt(strA + strB);
  });
  const result = nums.join("");
  return result[0] === "0" ? "0" : result;
}
