/**
 * Time complexity: O(n ^ 2)
 * @param {number[]} arr
 * @returns
 */
const bubbleSort = (arr) => {
  for (let i = 0; i < arr.length - 1; i++) {
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        const temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  return arr;
};

/**
 * Time complexity: O(n log n)
 * @param {number[]} arr
 * @returns
 */
const mergeSort = (arr) => {
  if (arr.length <= 1) {
    // 이미 정렬된 경우
    return arr;
  }
  // 중간을 기점으로 나눔
  const mid = Math.floor(arr.length / 2);
  const left = arr.slice(0, mid);
  const right = arr.slice(mid);

  const leftArr = mergeSort(left);
  const rightArr = mergeSort(right);
  // 병합
  return merge(leftArr, rightArr);
};

const merge = (leftArr, rightArr) => {
  const sortedArray = [];
  let leftIdx = 0,
    rightIdx = 0;

  while (leftIdx < leftArr.length && rightIdx < rightArr.length) {
    if (leftArr[leftIdx] < rightArr[rightIdx]) {
      sortedArray.push(leftArr[leftIdx]);
      leftIdx += 1;
    } else {
      sortedArray.push(rightArr[rightIdx]);
      rightIdx += 1;
    }
  }

  // 남아있는 요소 추가
  while (leftIdx < leftArr.length) {
    sortedArray.push(leftArr[leftIdx]);
    leftIdx += 1;
  }
  while (rightIdx < rightArr.length) {
    sortedArray.push(rightArr[rightIdx]);
    rightIdx += 1;
  }

  return sortedArray;
};

console.log(bubbleSort([4, 2, 3, 5, 1]));
console.log(mergeSort([4, 2, 3, 5, 1]));
