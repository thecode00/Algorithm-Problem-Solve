# https://leetcode.com/problems/jump-game-iv/


from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        index_dict = defaultdict(list)
        dp = [float("inf") for _ in range(len(arr))]
        for idx, num in enumerate(arr):
            index_dict[num].append(idx)

        queue = deque([0])
        dp[0] = 0   # Start point
        while queue:
            cur = queue.popleft()
            if cur == len(arr) - 1:  # We use BFS so first reach is fastest jump
                break
            # Use backtracking
            if cur - 1 >= 0 and dp[cur] + 1 < dp[cur - 1]:
                queue.append(cur - 1)
                dp[cur - 1] = dp[cur] + 1
            if cur + 1 < len(arr) and dp[cur] + 1 < dp[cur + 1]:
                queue.append(cur + 1)
                dp[cur + 1] = dp[cur] + 1
            for idx in index_dict[arr[cur]]:
                if idx != cur and dp[cur] + 1 < dp[idx]:
                    queue.append(idx)
                    dp[idx] = dp[cur] + 1
            index_dict[arr[cur]] = []   # After jump same value index clear list for prevent revisit
        print(dp)
        return dp[-1]
