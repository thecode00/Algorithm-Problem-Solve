// https://leetcode.com/problems/counter-ii/submissions/946844337/


type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    let changeNumber: number = init
    return {
        increment: () => {
            return ++changeNumber
        },
        decrement: () => {
            return --changeNumber;
        },
        reset: () => {
            changeNumber = init
            return changeNumber
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */