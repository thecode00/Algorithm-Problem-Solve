// https://leetcode.com/problems/daily-temperatures/description/

class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] answer = new int[temperatures.length];
        List<Integer> stack = new ArrayList<>();
        // Update the result if the current temperature warmer
        for (int idx = 0; idx < temperatures.length; idx++){
            while (!stack.isEmpty() && temperatures[idx] > temperatures[stack.get(stack.size() - 1)]){
                int i = stack.remove(stack.size() - 1);
                answer[i] = idx - i;
            }

            stack.add(idx);
        }

        return answer;
    }
}