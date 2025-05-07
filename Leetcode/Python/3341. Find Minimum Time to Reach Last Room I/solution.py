
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
