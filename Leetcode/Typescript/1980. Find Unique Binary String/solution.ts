// https://leetcode.com/problems/find-unique-binary-string/description

function findDifferentBinaryString(nums: string[]): string {
  const exist = new Set<number>();

  for (const binary of nums) {
    exist.add(parseInt(binary, 2));
  }

  for (let num = 0; num < 2 ** nums[0].length; num++) {
    if (!exist.has(num)) {
      return num.toString(2).padStart(nums[0].length, "0");
    }
  }

  return "Error";
}
