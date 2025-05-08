
# BFS
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        dp = [[float("inf")] * len(moveTime[0]) for _ in range(len(moveTime))]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        queue = deque()
        queue.append((0, 0, 0))

        while queue:
            cur_x, cur_y, cur_time = queue.popleft()

            for idx in range(4):
                new_x = cur_x + dx[idx]
                new_y = cur_y + dy[idx]

                if 0 <= new_x < len(moveTime[0]) and 0 <= new_y < len(moveTime):
                    next_time = cur_time
                    if moveTime[new_y][new_x] > next_time:
                        next_time = moveTime[new_y][new_x]
                    next_time += 1
                    if next_time < dp[new_y][new_x]:
                        queue.append((new_x, new_y, next_time))
                        dp[new_y][new_x] = next_time
        
        return dp[-1][-1]

# Dijkstra
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dp = [[-1] * m for _ in range(n)]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        heap = [(0, 0, 0)]

        while heap:
            cur_time, cur_col, cur_row = heapq.heappop(heap)

            if cur_col == m - 1 and cur_row == n - 1:
                return cur_time
                
            for idx in range(4):
                new_col = cur_col + dx[idx]
                new_row = cur_row + dy[idx]

                if 0 <= new_col < m and 0 <= new_row < n:
                    next_time = cur_time
                    if moveTime[new_row][new_col] > next_time:
                        next_time = moveTime[new_row][new_col]
                    
                    next_time += 1

                    if dp[new_row][new_col] == -1 or dp[new_row][new_col] > next_time:
                        heapq.heappush(heap, (next_time, new_col, new_row))
                        dp[new_row][new_col] = next_time
            
        