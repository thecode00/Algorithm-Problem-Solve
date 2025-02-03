// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

// Space: O(1)
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  for (let idx = 0; idx < arr.length; idx++) {
    arr[idx] = fn(arr[idx], idx);
  }
  return arr;
}
// Space: O(1)
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  arr.forEach((ele: number, idx: number) => {
    arr[idx] = fn(ele, idx);
  });
  return arr;
}

// Space: O(N)
function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  return arr.reduce((arr, element, index) => {
    arr[index] = fn(element, index);
    return arr;
  }, []);
}
