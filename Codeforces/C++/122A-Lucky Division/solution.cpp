// https://codeforces.com/problemset/problem/122/A

#include <iostream>

bool isLucky(int num);

int main(int argc, char const *argv[])
{
    int num;
    std::cin >> num;

    for (int div = 1; div <= num; div++)
    {
        if (num % div == 0 && isLucky(div))
        {
            std::cout << "YES";
            return 0;
        }
    }

    std::cout << "NO";
    return 0;
}

bool isLucky(int num)
{
    while (num > 0)
    {
        int r = num % 10;

        if (r != 4 && r != 7)
        {
            return false;
        }
        num /= 10;
    }

    return true;
}