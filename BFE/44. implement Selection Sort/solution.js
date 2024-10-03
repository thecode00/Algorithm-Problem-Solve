// https://bigfrontend.dev/problem/implement-Selection-Sort

/**
 * @param {number[]} arr
 */
function selectionSort(arr) {
  for (let left = 0; left < arr.length; left++) {
    let minIndex = left;
    for (let right = left; right < arr.length; right++) {
      if (arr[right] < arr[minIndex]) {
        minIndex = right;
      }
    }
    [arr[minIndex], arr[left]] = [arr[left], arr[minIndex]];
  }
}
