// https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution {
    public String longestPalindrome(String s) {
        int maxSize = 0;
        int palinIndex = 0;

        for (int idx = 0; idx < s.length(); idx++){
            int left = idx - 1;
            int right = idx;

            // Find same s[idx] character palindrome
            while (right < s.length() && s.charAt(right) == s.charAt(idx)) {
                right += 1;
            }

            // Find palindrome not same character s[idx]
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)){
                left -= 1;
                right += 1;
            }
            // [left + 1 ~ right - 1] is palindrome
            if (right - left - 1 > maxSize){
                maxSize = right - left - 1;
                palinIndex = left + 1;
            }
        }

        return s.substring(palinIndex, palinIndex + maxSize);
    }
}