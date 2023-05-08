// https://cses.fi/problemset/task/1623

#include <iostream>
#include <vector>

int n;
std::vector<long long> apples;

long long searchDiff(long long group1, long long group2, int idx)
{
    if (idx == n)
    {
        return std::abs(group1 - group2);
    }
    return std::min( // Compare Group1 got current apple, Group2 got current apple
        searchDiff(group1 + apples[idx], group2, idx + 1),
        searchDiff(group1, group2 + apples[idx], idx + 1));
}

int main(int argc, char const *argv[])
{
    std::cin >> n;
    long long input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        apples.push_back(input);
    }
    std::cout << searchDiff(0, 0, 0);
    return 0;
}
