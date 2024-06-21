// https://leetcode.com/problems/3sum/submissions/1295657048/

class Solution {    // Two pointer
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();

        for (int idx = 0; idx < nums.length; idx++) {
            // Prevent duplicate
            if (idx != 0 && nums[idx] == nums[idx - 1]){
                continue; 
            }
            int left = idx + 1;
            int right = nums.length - 1;

            while (left < right){
                int total = nums[idx] + nums[left] + nums[right];

                if (total < 0){
                    left += 1;
                } else if (total > 0){
                    right -= 1;
                } else {
                    answer.add(Arrays.asList(nums[idx], nums[left], nums[right]));
                    // Prevent duplicate
                    while (left < right && nums[left] == nums[left + 1]){
                        left += 1;
                    }
                    while (left < right && nums[right] == nums[right - 1]){
                        right -= 1;
                    }
                    right -= 1;
                    left += 1;
                }
            }
        }

        return answer;
    }
}