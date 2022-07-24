// https://www.acmicpc.net/problem/10871

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, x, a;
    scanf("%d %d", &n, &x);
    int array[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &a);
        if (a < x)
            printf("%d ", a);
    }
}