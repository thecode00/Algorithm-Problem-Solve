// https://cses.fi/problemset/task/1660

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n, target;
    std::cin >> n >> target;
    std::vector<int> array;
    int input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        array.emplace_back(input);
    }
    // Sliding window
    int left = 0, right = 0, total = 0, answer = 0;
    while (left < n)
    {
        while (right < n && total < target)
        {
            total += array[right];
            right += 1;
        }
        if (total == target)
        {
            answer += 1;
        }
        total -= array[left];
        left += 1;
    }
    std::cout << answer;

    return 0;
}
