// https://cses.fi/problemset/task/1091

#include <iostream>
#include <algorithm>
#include <set>

int main(int argc, char const *argv[])
{
    int tickets, customers;
    std::cin >> tickets >> customers;
    std::multiset<int> count;
    int input;
    for (int i = 0; i < tickets; i++)
    {
        std::cin >> input;
        count.insert(input); // Save ticket count
    }
    for (int i = 0; i < customers; i++)
    {
        std::cin >> input;
        auto index = count.upper_bound(input); // index is iter
        if (index == count.begin())            // Not enough for buy ticket
        {
            std::cout << "-1\n";
        }
        else
        {
            index--;
            std::cout << *index << "\n";
            count.erase(index);
        }
    }

    return 0;
}
