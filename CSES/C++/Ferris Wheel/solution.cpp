// https://cses.fi/problemset/task/1090

#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char const *argv[])
{
    int n, x; // Number of children, maximum allowed weight
    std::cin >> n >> x;
    std::vector<int> children(n, 0);
    for (int i = 0; i < n; i++)
    {
        int input;
        std::cin >> input;
        children[i] = input;
    }
    std::sort(children.begin(), children.end());

    int left = 0, right = n - 1, count = 0;
    while (left <= right)
    {
        count += 1;
        if (children[left] + children[right] <= x)
        {
            left += 1;
        }
        right -= 1;
    }
    std::cout << count;
    return 0;
}
