// https://cses.fi/problemset/task/1647

// TODO: Solve
#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n, q; // Length of array, number of queries
    std::cin >> n >> q;

    std::vector<long long> arr;
    for (int i = 0; i < n; i++)
    {
        long long input;
        std::cin >> input;
        arr.push_back(input);
    }

    std::vector<int> height;
    for (int i = 0; i < n + 1; i++)
    {
        if (i > 1)
        {
            height.push_back((i >> 1) + 1);
        }
        else
        {
            height.push_back(0);
        }
    }
    std::cout << 14;
    int step = 1;
    std::vector<std::vector<long long>> table(height.back() + 1, std::vector<long long>(n, -1));
    for (int y = 0; y < height.back() + 1; y++)
    {
        for (int x = 0; x < n; x++)
        {
            if (y == 0)
            {
                table[0].push_back(arr[x]);
            }
            else if (x + step < n)
            {
                table[y].push_back(std::min(table[y - 1][x], table[y - 1][x + step]));
            }
        }
        step <<= 1;
    }

    for (int i = 0; i < q; i++)
    {
        int a, b;
        std::cin >> a >> b;
        // Make to 0-index
        a -= 1;
        b -= 1;
        int row = height[b - a + 1];
        std::cout << std::min(table[row][a], table[row][b + 1 - (1 << row)]);
    }
    return 0;
}
