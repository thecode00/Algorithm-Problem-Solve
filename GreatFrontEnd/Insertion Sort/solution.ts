// https://www.greatfrontend.com/questions/javascript/insertion-sort

export default function insertionSort(arr: Array<number>): Array<number> {
  for (let idx = 1; idx < arr.length; idx++) {
    if (arr[idx] >= arr[idx - 1]) continue;

    let currentIdx = idx;
    for (let sortedIdx = idx - 1; sortedIdx >= 0; sortedIdx--) {
      // Find insert index and swap
      if (arr[sortedIdx] > arr[currentIdx]) {
        const temp = arr[sortedIdx];
        arr[sortedIdx] = arr[currentIdx];
        arr[currentIdx] = temp;
        currentIdx -= 1;
      } else {
        break;
      }
    }
  }

  return arr;
}
