# https://leetcode.com/problems/minimum-penalty-for-a-shop/description/

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        count_n = customers.count("N")
        # The initial value is initialized to the value when shop close after all schedules are completed
        min_penalty, min_penalty_hour = count_n, len(customers)
        close_penalty = 0
        for i in range(len(customers) - 1, -1, -1):
            if customers[i] == 'Y':
                close_penalty += 1
            else:
                count_n -= 1
            # We need return earliest hour incur a minimum penalty o even when min_penalty is equal to the penalty update hour
            if close_penalty + count_n <= min_penalty:
                min_penalty_hour = i
                min_penalty = close_penalty + count_n

        return min_penalty_hour
