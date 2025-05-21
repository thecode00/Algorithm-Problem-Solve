// https://codeforces.com/problemset/problem/160/A

#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;

    std::cin >> n;

    std::vector<int> coins(n);
    int total = 0;
    for (int idx = 0; idx < n; idx++)
    {
        int coin;
        std::cin >> coin;

        total += coin;
        coins[idx] = coin;
    }

    std::sort(coins.rbegin(), coins.rend());

    int myCoins = 0;
    for (int idx = 0; idx < n; idx++)
    {
        myCoins += coins[idx];
        total -= coins[idx];

        if (myCoins > total)
        {
            std::cout << idx + 1;
            break;
        }
    }
    std::cout << "\n";
    return 0;
}
