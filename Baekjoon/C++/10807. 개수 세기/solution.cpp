// https://www.acmicpc.net/problem/10807

#include <iostream>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, v, c;
    scanf("%d", &n);
    int array[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &array[i]);
    }
    scanf("%d", &v);
    c = count(array, array + n, v);
    printf("%d", c);
}