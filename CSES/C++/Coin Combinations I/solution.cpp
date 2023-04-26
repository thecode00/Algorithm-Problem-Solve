// https://cses.fi/problemset/task/1635

#include <iostream>
#include <vector>

#define mod 1000000007

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
    dp[0] = 1;
    for (int i = 1; i < target + 1; i++)
    {
        for (auto coin : coins)
        {
            if (i - coin >= 0)
            {
                dp[i] += dp[i - coin];
                dp[i] %= mod;
            }
        }
    }
    std::cout << dp[target];
    return 0;
}
