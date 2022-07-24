// https://www.acmicpc.net/problem/10952

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int a, b;
    while (true)
    {
        cin >> a >> b;
        if (a == 0 & b == 0)
        {
            break;
        }
        printf("%d\n", a + b);
    }
}
