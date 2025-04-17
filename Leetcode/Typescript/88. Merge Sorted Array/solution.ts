// https://leetcode.com/problems/merge-sorted-array/description/

/**
 Do not return anything, modify nums1 in-place instead.
 */
function merge(nums1: number[], m: number, nums2: number[], n: number): void {
  let insertIndex = nums1.length - 1;
  // Change to 0-index
  m -= 1;
  n -= 1;

  while (0 <= n) {
    if (0 <= m) {
      if (nums1[m] < nums2[n]) {
        nums1[insertIndex] = nums2[n];
        n -= 1;
      } else {
        nums1[insertIndex] = nums1[m];
        m -= 1;
      }
    } else {
      nums1[insertIndex] = nums2[n];
      n -= 1;
    }
    insertIndex -= 1;
  }
}
