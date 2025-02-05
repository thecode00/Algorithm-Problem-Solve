// https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description

function areAlmostEqual(s1: string, s2: string): boolean {
  const diff: string[][] = [];

  for (let idx = 0; idx < s1.length; idx++) {
    if (s1[idx] !== s2[idx]) {
      diff.push([s1[idx], s2[idx]]);
    }
  }

  return (
    diff.length === 0 || (diff.length === 2 && hasSameElement(diff[0], diff[1]))
  );
}

function hasSameElement(arr1: string[], arr2: string[]): boolean {
  const arrLength = arr1.length;
  for (let idx = 0; idx < arrLength; idx++) {
    if (arr1[idx] !== arr2[arrLength - idx - 1]) {
      return false;
    }
  }

  return true;
}
