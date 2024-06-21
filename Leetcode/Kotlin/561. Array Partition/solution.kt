// https://leetcode.com/problems/array-partition/

class Solution {
    fun arrayPairSum(nums: IntArray): Int {
        nums.sort()
        var answer = 0

        for ((idx, num) in nums.withIndex()){
            if (idx % 2 == 0){
                answer += num
            }
        }

        return answer
    }
}