// https://codeforces.com/problemset/problem/282/A

#include <iostream>
#include <string>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    int num = 0;

    for (int i = 0; i < n; i++)
    {
        std::string oper;
        std::cin >> oper;

        if (oper[1] == '+')
        {
            num += 1;
        }
        else
        {
            num -= 1;
        }
    }

    std::cout << num;
    return 0;
}
