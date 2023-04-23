// https://cses.fi/problemset/task/1638

#include <iostream>
#include <vector>
#include <string>

const int MOD = 1e9 + 7;

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;
    char input;
    std::vector<std::vector<char>> board(n, std::vector<char>(n));
    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < n; x++)
        {
            std::cin >> board[y][x];
        }
    }
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 0));
    for (int y = 0; y < n; y++)
    {
        for (int x = 0; x < n; x++)
        {
            if (board[y][x] == '*') // Pass trap
            {
                continue;
            }
            if (y == 0 && x == 0)
            {
                dp[y][x] = 1;
            }
            else if (y == 0)
            {
                dp[y][x] = dp[y][x - 1];
            }
            else if (x == 0)
            {
                dp[y][x] = dp[y - 1][x];
            }
            else
            {
                dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD; // Add path from top and left
            }
        }
    }
    std::cout << dp[n - 1][n - 1];
    return 0;
}
