// https://www.acmicpc.net/problem/2884

#include <iostream>

int main()
{
    int hour, minute;
    std::cin >> hour >> minute;

    if (minute < 45)
    {
        if (hour == 0)
        {
            hour = 23;
        }
        else
        {
            hour -= 1;
        }
        minute += 60 - 45;
    }
    else
    {
        minute -= 45;
    }
    std::cout << hour << " " << minute;
}
