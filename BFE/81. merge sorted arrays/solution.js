// https://bigfrontend.dev/problem/merge-sorted-arrays

/**
 * @param {number[][]} arrList
 * non-descending integer array
 * @return {number[]}
 */
function merge(arrList) {
  if (!arrList || arrList.length === 0) {
    return [];
  }

  if (arrList.length === 1) {
    return arrList[0];
  } else if (arrList.length === 2) {
    return mergeTwoList(arrList[0], arrList[1]);
  }

  const half = Math.floor(arrList.length / 2);
  return mergeTwoList(
    merge(arrList.slice(0, half)),
    merge(arrList.slice(half, arrList.length))
  );
}

function mergeTwoList(l1, l2) {
  let idx1 = 0,
    idx2 = 0;
  const result = [];

  while (idx1 < l1.length || idx2 < l2.length) {
    if (idx1 >= l1.length || l1[idx1] > l2[idx2]) {
      result.push(l2[idx2]);
      idx2 += 1;
    } else {
      result.push(l1[idx1]);
      idx1 += 1;
    }
  }

  return result;
}
