// https://cses.fi/problemset/task/1648

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    // Fast input, output
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);

    int n, q;
    std::cin >> n >> q;
    std::vector<int> nums;
    nums.push_back(0); // Makes nums 1-index

    int input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        nums.push_back(input);
    }
    std::vector<long long> dp(n + 1, 0);
    for (int i = 1; i <= n; i++)
    {
        dp[i] = dp[i - 1] + nums[i];
    }

    int cmd, a, b;
    for (int i = 0; i < q; i++)
    {
        std::cin >> cmd >> a >> b;
        if (cmd == 1) // Update value
        {
            int prev = nums[a];
            for (int j = a; j <= n; j++)
            {
                dp[j] += b - prev;
            }
        }
        else
        {
            std::cout << dp[b] - dp[a - 1] << std::endl;
        }
    }
    return 0;
}
