// https://cses.fi/problemset/task/1634

#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 10000000

int main(int argc, char const *argv[])
{
    int n, x;
    std::cin >> n >> x;

    std::vector<int> dp(x + 1, MAX);
    dp[0] = 0;
    std::vector<int> coins;
    for (int i = 0; i < n; i++)
    {
        int input;
        std::cin >> input;
        coins.push_back(input);
    }
    for (int i = 1; i < x + 1; i++)
    {
        for (auto coin : coins)
        {
            if (i - coin >= 0)
            {
                dp[i] = std::min(dp[i - coin] + 1, dp[i]);
            }
        }
    }
    if (dp[x] == MAX)
    {
        std::cout << -1;
    }
    else
    {
        std::cout << dp[x];
    }
    return 0;
}
