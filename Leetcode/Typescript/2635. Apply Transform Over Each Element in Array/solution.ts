// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    for (let idx = 0; idx < arr.length; idx++){
        arr[idx] = fn(arr[idx], idx)
    }
    return arr
};