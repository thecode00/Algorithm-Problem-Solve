// https://leetcode.com/problems/valid-parentheses/description/

class Solution {
    fun isValid(s: String): Boolean {
        val parenthesisHash: Map<Char, Char> = mapOf(
            ')' to '(',
            ']' to '[',
            '}' to '{'
        )

        val stack = ArrayDeque<Char>();

        for (idx in s.indices){
            val p = s[idx]

            if (parenthesisHash.containsKey(p)){
                if (stack.isEmpty() || stack.last() != parenthesisHash[p]){
                    return false;
                }
                stack.removeLast()
                continue
            }

            stack.add(p)
        }
        // Check remain open parenthesis
        return stack.isEmpty()
    }
}