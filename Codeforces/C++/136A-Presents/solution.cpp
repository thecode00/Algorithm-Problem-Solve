// https://codeforces.com/problemset/problem/136/A

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::vector<int> receive(n);

    for (int idx = 0; idx < n; idx++)
    {
        int give;
        std::cin >> give;

        receive[give - 1] = idx + 1;
    }

    for (int idx = 0; idx < n; idx++)
    {
        std::cout << receive[idx] << " ";
    }
    std::cout << "\n";
    return 0;
}
