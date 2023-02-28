// https://www.acmicpc.net/problem/2747

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n;
    int prev = 0, cur = 1;
    int temp;
    cin >> n;
    if (n <= 1)
    {
        cout << n;
        return 0;
    }

    for (int i = 2; i <= n; i++)
    {
        temp = cur;
        cur += prev;
        prev = temp;
    }
    cout << cur;
    return 0;
}
