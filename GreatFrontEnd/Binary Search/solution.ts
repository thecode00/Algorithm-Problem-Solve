// https://www.greatfrontend.com/questions/javascript/binary-search

/**
 * @param arr The input integer array to be searched.
 * @param target The target integer to search within the array.
 * @return The index of target element in the array, or -1 if not found.
 */
export default function binarySearch(
  arr: Array<number>,
  target: number
): number {
  arr.sort((a, b) => a - b);
  let start = 0,
    end = arr.length - 1;

  while (start <= end) {
    const mid = Math.floor((start + end) / 2);
    if (arr[mid] === target) {
      return mid;
    } else if (arr[mid] > target) {
      end = mid - 1;
    } else {
      start = mid + 1;
    }
  }

  return -1;
}
