// https://leetcode.com/problems/promise-time-limit/
// Ref: https://leetcode.com/problems/promise-time-limit/solutions/3406548/easy-promise-race-solution/?utm_campaign=PostD12&utm_medium=Post&utm_source=Post&gio_link_id=nombN5Z9&orderBy=most_votes

type Fn = (...params: any[]) => Promise<any>;

function timeLimit(fn: Fn, t: number): Fn {
	return async function(...args) {
        return new Promise<any[]>((resolve, reject) => {
            setTimeout(() => {
                reject("Time Limit Exceeded")
            }, t)
            fn(...args).then(resolve).catch(reject)
        })
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */