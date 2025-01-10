// https://leetcode.com/problems/filter-elements-from-array/

type Fn = (n: number, i: number) => any;

function filter(arr: number[], fn: Fn): number[] {
  const newArray: number[] = [];

  arr.forEach((item, idx) => {
    if (fn(item, idx)) {
      newArray.push(item);
    }
  });

  return newArray;
}

function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
  const newArray: number[] = [];
  let index: number = 0;
  for (const num of arr) {
    if (fn(num, index)) {
      newArray.push(num);
    }
    index += 1;
  }
  return newArray;
}

function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
  return arr.filter((element: number, index: number) => fn(element, index));
}
