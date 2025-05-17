// https://codeforces.com/problemset/problem/1462/A

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++)
    {
        int n;
        std::cin >> n;

        std::vector<int> vec(n);

        for (int idx = 0; idx < n; idx++)
        {
            std::cin >> vec[idx];
        }

        int left = 0;
        int right = vec.size() - 1;

        std::vector<int> original;

        while (left < right)
        {
            original.emplace_back(vec[left]);
            original.emplace_back(vec[right]);

            left += 1;
            right -= 1;
        }

        if (left == right)
        {
            original.emplace_back(vec[left]);
        }

        for (int idx = 0; idx < n; idx++)
        {
            std::cout << original[idx] << " ";
        }
        std::cout << "\n";
    }
    return 0;
}
