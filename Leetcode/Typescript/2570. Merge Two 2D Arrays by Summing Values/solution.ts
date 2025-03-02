// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description

function mergeArrays(nums1: number[][], nums2: number[][]): number[][] {
  const result: number[][] = [];
  const idMap = new Map<number, number>();

  for (const [id, num] of nums1) {
    idMap.set(id, (idMap.get(id) || 0) + num);
  }

  for (const [id, num] of nums2) {
    idMap.set(id, (idMap.get(id) || 0) + num);
  }

  const keys = Array.from(idMap.keys());
  keys.sort((a, b) => a - b);

  for (const key of keys) {
    result.push([key, idMap.get(key)!]);
  }

  return result;
}
