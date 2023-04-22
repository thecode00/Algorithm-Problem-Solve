// https://cses.fi/problemset/task/1636

#include <iostream>
#include <vector>

const int MOD = 1e9 + 7;

int main(int argc, char const *argv[])
{
    int n, target;
    std::cin >> n >> target;
    std::vector<int> coins;
    for (int i = 0; i < n; i++)
    {
        int input;
        std::cin >> input;
        coins.push_back(input);
    }
    std::vector<long long> dp(target + 1, 0);
    dp[0] = 1; // Base case
    for (auto coin : coins)
    {
        for (int i = 0; i < target + 1; i++)
        {
            if (i - coin >= 0)
            {
                dp[i] += dp[i - coin];
                dp[i] %= MOD;
            }
        }
    }
    std::cout << dp[target];
    return 0;
}
