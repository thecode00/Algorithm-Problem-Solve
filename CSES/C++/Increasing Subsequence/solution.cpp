// https://cses.fi/problemset/task/1145
// Ref: https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/

#include <iostream>
#include <vector>
#include <algorithm>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;
    std::vector<long long> numbers;
    for (int i = 0; i < n; i++)
    {
        int input;
        std::cin >> input;
        numbers.push_back(input);
    }
    std::vector<int> stack;
    for (auto num : numbers)
    {
        if (stack.empty() || stack.back() < num)
        {
            stack.push_back(num);
        }
        else
        {
            int index = std::lower_bound(stack.begin(), stack.end(), num) - stack.begin();
            stack[index] = num;
        }
    }
    std::cout << stack.size();
    return 0;
}