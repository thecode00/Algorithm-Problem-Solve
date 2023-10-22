// https://leetcode.com/problems/valid-palindrome/description/

class Solution {
    fun isPalindrome(s: String): Boolean {
        var start: Int = 0
        var end: Int = s.length - 1
        while (start < end){
            when {
                // If current index is not char or digit move pointer
                !Character.isLetterOrDigit(s[start]) -> start += 1
                !Character.isLetterOrDigit(s[end]) -> end -= 1
                else -> {
                    // Check palindrome
                    if (Character.toLowerCase(s[start]) != Character.toLowerCase(s[end])){
                        return false
                    }
                    start += 1
                    end -= 1
                }
            }
        }
        return true
    }
}