// https://cses.fi/problemset/task/1070

#include <iostream>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;
    if (n == 1)
    {
        std::cout << 1;
        return 0;
    }
    else if (n <= 3)
    {
        std::cout << "NO SOLUTION";
        return 0;
    }

    // Print even number and odd number
    for (int even = 2; even <= n; even += 2)
    {
        std::cout << even << " ";
    }
    for (int odd = 1; odd <= n; odd += 2)
    {
        std::cout << odd << " ";
    }
    return 0;
}
