// https://cses.fi/problemset/task/1083

#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;
    std::vector<int> v;
    for (int i = 0; i < n - 1; i++)
    {
        int num;
        std::cin >> num;
        v.push_back(num);
    }
    std::sort(v.begin(), v.end());
    int check = 1;
    for (auto num : v)
    {
        if (check != num)
        {
            std::cout << check;
            return 0;
        }
        check += 1;
    }
    std::cout << n;
    return 0;
}
