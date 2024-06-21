// https://leetcode.com/problems/valid-parentheses/description/

class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> parenthesisHash = new HashMap<>();
        parenthesisHash.put('}', '{');
        parenthesisHash.put(']', '[');
        parenthesisHash.put(')', '(');

        Deque<Character> stack = new ArrayDeque<>();

        for (int idx = 0; idx < s.length(); idx++) {
            char p = s.charAt(idx);

            if (parenthesisHash.containsKey(p)) {
                if (stack.isEmpty() || stack.pop() != parenthesisHash.get(p)) {
                    return false;
                }
                continue;
            }

            stack.add(p);
        }

        // Check remain open parenthesis
        return stack.isEmpty();
    }
}