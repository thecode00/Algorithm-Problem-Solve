// https://cses.fi/problemset/task/1637

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::vector<int> dp(n + 1, 1e9);
    dp[n] = 0; // Base case
    for (int num = n; num > 0; num--)
    {
        int temp = num;
        while (temp > 0)
        {
            int r = temp % 10;
            temp /= 10;
            if (r != 0)
            {
                dp[num - r] = std::min(dp[num - r], dp[num] + 1);
            }
        }
    }
    std::cout << dp[0];
    return 0;
}
