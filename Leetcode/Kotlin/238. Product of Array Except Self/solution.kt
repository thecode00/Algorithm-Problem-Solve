// https://leetcode.com/problems/product-of-array-except-self/description/

class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        var answer = IntArray(nums.size)

        var mul = 1
        // By assigning the current index to answer before multiplying by mul, we store the product of the numbers to the left of the current index
        for (idx in nums.indices){
            answer[idx] = mul
            mul *= nums[idx]
        }

        mul = 1
        for (idx in nums.indices.reversed()){
            answer[idx] *= mul
            mul *= nums[idx]
        }

        return answer
    }
}