// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

// Binary search
function twoSum(numbers: number[], target: number): number[] {
  for (let idx = 0; idx < numbers.length; idx++) {
    const newTarget = target - numbers[idx];
    let start = idx + 1,
      end = numbers.length - 1;

    while (start <= end) {
      const mid = start + Math.floor((end - start) / 2);

      if (numbers[mid] === newTarget) {
        return [idx + 1, mid + 1];
      } else if (numbers[mid] > newTarget) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }
  }

  return [-1, -1];
}

// Two pointer
function twoSum(numbers: number[], target: number): number[] {
  let start = 0,
    end = numbers.length - 1;

  while (start < end) {
    const twoSum = numbers[start] + numbers[end];

    if (twoSum > target) {
      end -= 1;
    } else if (twoSum < target) {
      start += 1;
    } else {
      break;
    }
  }

  return [start + 1, end + 1];
}
