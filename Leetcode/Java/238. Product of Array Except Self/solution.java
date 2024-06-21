// https://leetcode.com/problems/product-of-array-except-self/description/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int mul = 1;

        // By assigning the current index to answer before multiplying by mul, we store the product of the numbers to the left of the current index
        for (int idx = 0; idx < nums.length; idx++){
            answer[idx] = mul;
            mul *= nums[idx];
        }

        mul = 1;
        for (int idx = nums.length - 1; idx >= 0; idx--){
            answer[idx] *= mul;
            mul *= nums[idx];
        }

        return answer;
    }
}