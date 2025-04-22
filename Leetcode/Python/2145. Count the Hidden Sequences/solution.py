# https://leetcode.com/problems/count-the-hidden-sequences/description

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_sum = 0 
        range_min = range_max = 0  

        # Compute prefix sums and track the min and max values
        for diff in differences:
            prefix_sum += diff
            range_min = min(range_min, prefix_sum) 
            range_max = max(range_max, prefix_sum)  

        sequence_range = range_max - range_min

        # Calculate how many valid starting values arr[0] can take
        # so that all elements stay within [lower, upper]
        hidden_sequences = upper - lower - sequence_range + 1

        # If the count is negative, it means no valid sequence exists
        return 0 if hidden_sequences < 0 else hidden_sequences