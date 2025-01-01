# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        day7, day30 = deque(), deque()
        cost = 0

        for day in days:
            while day7 and day7[0][0] <= day - 7:
                day7.popleft()
            while day30 and day30[0][0] <= day - 30:
                day30.popleft()

            day7.append((day, cost + costs[1]))
            day30.append((day, cost + costs[2]))
            cost = min(cost + costs[0], day7[0][1], day30[0][1])

        return cost


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]
        cover = [1, 7, 30]
        dp = [float("inf") for _ in range(days[-1] + 1)]
        for idx, day in enumerate(days):
            for i in range(3):
                for d in range(cover[i]):
                    if d + day > max_day:
                        break
                    if idx > 0:
                        dp[day + d] = min(dp[days[idx - 1]] +
                                          costs[i], dp[day + d])
                    else:
                        dp[day + d] = min(dp[day + d], costs[i])

        print(dp)
        return 0


class Solution:  # Optimized code, Ref: https://leetcode.com/problems/minimum-cost-for-tickets/solutions/810806/python-dp-solution-explanation/?orderBy=most_votes
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]
        dp = [0 for _ in range(max_day + 1)]
        days_set = set(days)
        for idx in range(1, max_day + 1):
            if idx not in days_set:
                dp[idx] = dp[idx - 1]
            else:
                dp[idx] = min(
                    dp[max(0, idx - 1)] + costs[0],  # 1-day pass
                    dp[max(0, idx - 7)] + costs[1],  # 7-day pass
                    dp[max(0, idx - 30)] + costs[2]  # 30-day pass
                )
        return dp[max_day]
