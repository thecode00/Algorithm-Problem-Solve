// https://bigfrontend.dev/problem/remove-duplicates-from-an-array

/**
 * @param {any[]} arr
 */
function deduplicate(arr) {
  const used = new Set();
  let pushIndex = 0;

  for (let idx = 0; idx < arr.length; idx++) {
    if (!used.has(arr[idx])) {
      used.add(arr[idx])[(arr[idx], arr[pushIndex])] = [
        arr[pushIndex],
        arr[idx],
      ];
      pushIndex += 1;
    }
  }

  while (pushIndex !== arr.length) {
    arr.pop();
  }

  return arr;
}
