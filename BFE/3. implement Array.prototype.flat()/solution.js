// https://bigfrontend.dev/problem/implement-Array-prototype.flat

// This is a JavaScript coding problem from BFE.dev
/**
 * @param { Array } arr
 * @param { number } depth
 * @returns { Array }
 */
function flat(arr, depth = 1) {
  // your imeplementation here
  const result = [];

  for (let idx = 0; idx < arr.length; idx++) {
    if (typeof arr[idx] === "object" && depth > 0) {
      result.push(...flat(arr[idx], depth - 1));
    } else {
      result.push(arr[idx]);
    }
  }

  return result;
}
