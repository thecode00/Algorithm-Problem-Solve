// https://leetcode.com/problems/filter-elements-from-array/

function filter(arr: number[], fn: (n: number, i: number) => any): number[] {
    const newArray: number[] = []
    let index: number = 0
    for (const num of arr) {
        if (fn(num, index)) {
            newArray.push(num)
        }
        index += 1
    }
    return newArray
};