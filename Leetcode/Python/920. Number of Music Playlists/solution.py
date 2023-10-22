# https://leetcode.com/problems/number-of-music-playlists/description/
MOD = int(1e9) + 7


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        # dp[i][j] = number of playlist with size of playlist i and unique songs j
        dp = [[0] * (n + 1) for _ in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal + 1):
            for j in range(1, min(n, i) + 1):
                # Add new unique song, n - (j - 1) = number of songs not in the playlist
                dp[i][j] = (dp[i - 1][j - 1] * (n - (j - 1))) % MOD
                if j > k:   # Add already used song
                    dp[i][j] += (dp[i - 1][j] * (j - k)) % MOD
        print(dp)
        return dp[-1][-1] % MOD
