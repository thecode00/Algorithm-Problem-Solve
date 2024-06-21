// https://leetcode.com/problems/product-of-array-except-self/description/

function productExceptSelf(nums: number[]): number[] {
  const answer = Array(nums.length);
  // By assigning the current index to answer before multiplying by mul, we store the product of the numbers to the left of the current index
  let mul = 1;
  for (let idx = 0; idx < nums.length; idx++) {
    answer[idx] = mul;
    mul *= nums[idx];
  }

  mul = 1;
  for (let idx = nums.length - 1; idx >= 0; idx--) {
    answer[idx] *= mul;
    mul *= nums[idx];
  }

  return answer;
}
