# https://leetcode.com/problems/maximum-swap/description

class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        max_idx = list(range(len(num_list)))
        length = len(num_list)
        max_idx[length - 1] = length - 1

        for idx in range(length - 2, -1, -1):
            # Need to swap with the rightmost number that is greater than your current number, 
            # so if the numbers are equal, you should record the index of the number on the right
            # If num = 3444, max_idx will be [3, 3, 3, 3]
            if int(num_list[idx]) <= int(num_list[max_idx[idx + 1]]):
                max_idx[idx] = max_idx[idx + 1]
            else:
                max_idx[idx] = idx

        for idx in range(length):
            max_index = max_idx[idx]
            if int(num_list[idx]) < int(num_list[max_index]):
                num_list[idx], num_list[max_index] = num_list[max_index], num_list[idx]
                break

        return int("".join(num_list))
