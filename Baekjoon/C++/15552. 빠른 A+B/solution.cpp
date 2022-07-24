// https://www.acmicpc.net/problem/15552

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, a, b;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d %d", &a, &b);
        printf("%d\n", a + b);
    }
}