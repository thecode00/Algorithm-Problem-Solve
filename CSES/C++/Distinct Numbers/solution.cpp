// https://cses.fi/problemset/task/1621

#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    long long n;
    std::cin >> n;
    std::vector<long long> arr;
    for (int i = 0; i < n; i++)
    {
        long long num;
        std::cin >> num;
        arr.push_back(num);
    }
    sort(arr.begin(), arr.end());
    long long check = -1;
    int count = 0;
    for (auto num : arr)
    {
        if (check != num)
        {
            count += 1;
            check = num;
        }
    }
    std::cout << count;
    return 0;
}
