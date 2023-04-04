// https://www.acmicpc.net/problem/2480

#include <algorithm>
#include <iostream>

int main()
{
    int a, b, c;
    int prize = 0;
    std::cin >> a >> b >> c;
    if (a == b && b == c)
    {
        prize += 10000 + a * 1000;
    }
    else if (a == b || a == c)
    {
        prize += 1000 + a * 100;
    }
    else if (b == c)
    {
        prize += 1000 + b * 100;
    }
    else
    {
        prize += std::max({ a, b, c }) * 100;
    }
    std::cout << prize;
}