// https://www.acmicpc.net/problem/8393

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n;
    int total = 0;
    cin >> n;
    for (int i = 1; i < n + 1; i++)
    {
        total += i;
    }
    cout << total;
    return 0;
}
