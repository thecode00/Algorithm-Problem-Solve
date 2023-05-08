// https://cses.fi/problemset/task/1094

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;
    std::vector<int> array;
    int input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        array.push_back(input);
    }
    long long count = 0;
    for (int idx = 1; idx < n; idx++)
    {
        if (array[idx - 1] > array[idx])
        {
            count += array[idx - 1] - array[idx];
            array[idx] = array[idx - 1]; // Update array value to previous large value
        }
    }
    std::cout << count;
    return 0;
}
