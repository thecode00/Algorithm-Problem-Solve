// https://cses.fi/problemset/task/1158

#include <iostream>
#include <vector>
#define MAX 1000
int prices[MAX];
int pages[MAX];

int main(int argc, char const *argv[])
{
    int n, maxPrice;
    std::cin >> n >> maxPrice;
    for (int idx = 0; idx < n; idx++)
    {
        std::cin >> prices[idx];
    }
    for (int idx = 0; idx < n; idx++)
    {
        std::cin >> pages[idx];
    }

    // dp[y][x] = maximum page with y books and total price x
    std::vector<std::vector<int>> dp(n + 1, std::vector<int>(maxPrice + 1, 0));
    for (int y = 1; y < n + 1; y++)
    {
        for (int x = 1; x < maxPrice + 1; x++)
        {
            if (x >= prices[y - 1])
            {
                dp[y][x] = std::max(dp[y - 1][x], dp[y - 1][x - prices[y - 1]] + pages[y - 1]); // Compare not choose book[y - 1] and choose book[y - 1]
            }
            else
            {
                dp[y][x] = dp[y - 1][x];
            }
        }
    }
    std::cout << dp[n][maxPrice];
    return 0;
}
