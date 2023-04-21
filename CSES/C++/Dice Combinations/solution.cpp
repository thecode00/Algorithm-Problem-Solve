// https://cses.fi/problemset/task/1633

#include <iostream>
#include <vector>
#define mod 1000000007

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    for (int i = 1; i < n + 1; i++)
    {
        for (int num = 1; num < 7; num++)
        {
            if (i - num >= 0)
            {
                dp[i] += dp[i - num];
                dp[i] %= mod;
            }
        }
    }
    std::cout << dp[n];
    return 0;
}
