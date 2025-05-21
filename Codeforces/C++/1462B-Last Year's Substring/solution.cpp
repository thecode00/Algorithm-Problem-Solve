// https://codeforces.com/problemset/problem/1462/B

#include <iostream>
#include <string>

int main()
{
    int t;
    std::cin >> t;
    std::string target = "2020";

    while (t--)
    {
        int n;
        std::cin >> n;
        std::string str;
        std::cin >> str;

        bool found = false;

        for (int i = 0; i <= 4; ++i)
        {
            std::string prefix = str.substr(0, i);
            std::string suffix = str.substr(n - (4 - i), 4 - i);
            if (prefix + suffix == target)
            {
                found = true;
                break;
            }
        }

        std::cout << (found ? "YES" : "NO") << "\n";
    }

    return 0;
}
