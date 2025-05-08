# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-ii/description

# Dijkstra
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dp = [[-1] * m for _ in range(n)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        dt = [1, 2]

        heap = [(0, 0, 0, 0)]

        while heap:
            cur_time, time_turn, cur_col, cur_row = heapq.heappop(heap)

            if cur_col == m - 1 and cur_row == n - 1:
                return cur_time
                
            for idx in range(4):
                new_col = cur_col + dx[idx]
                new_row = cur_row + dy[idx]

                if 0 <= new_col < m and 0 <= new_row < n:
                    next_time = cur_time
                    if moveTime[new_row][new_col] > next_time:
                        next_time = moveTime[new_row][new_col]
                    
                    next_time += dt[time_turn]
                    if new_col == m - 1 and new_row == n - 1:
                        return next_time

                    if dp[new_row][new_col] == -1 or dp[new_row][new_col] > next_time:
                        # Change move time
                        heapq.heappush(heap, (next_time, time_turn ^ 1, new_col, new_row))
                        dp[new_row][new_col] = next_time
            
        