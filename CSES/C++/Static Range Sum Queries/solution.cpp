// https://cses.fi/problemset/task/1646

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    // Formula = sum(a ~ b) = sum(0 ~ b) - sum(0 ~ (a - 1))
    int n, q; // Number of values and queries
    std::cin >> n >> q;
    std::vector<long long> prefix;
    prefix.push_back(0); // "Inserting a zero to satisfy the formula even when a is zero
    for (int i = 0; i < n; i++)
    {
        int num;
        std::cin >> num;
        prefix.push_back(prefix[i] + num);
    }

    for (int i = 0; i < q; i++)
    {
        int a, b;
        std::cin >> a >> b;
        std::cout << prefix[b] - prefix[a - 1] << "\n";
    }

    return 0;
}
