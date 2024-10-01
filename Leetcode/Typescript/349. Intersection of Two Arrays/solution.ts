// https://leetcode.com/problems/intersection-of-two-arrays/description/

function intersection(nums1: number[], nums2: number[]): number[] {
  const checked = new Set<number>();
  const result: number[] = [];
  nums2.sort((a, b) => a - b);

  for (const num of nums1) {
    if (checked.has(num)) {
      continue;
    }

    let start = 0,
      end = nums2.length - 1;
    while (start <= end) {
      const mid = start + Math.floor((end - start) / 2);

      if (nums2[mid] === num) {
        result.push(num);
        break;
      } else if (nums2[mid] > num) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }

    checked.add(num);
  }

  return result;
}
