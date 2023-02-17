// https://www.acmicpc.net/problem/2908

#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    string a, b;
    cin >> a >> b;
    for (int i = 3; i >= 0; i--)
    {
        if (a[i] > b[i])
        {
            reverse(a.begin(), a.end());
            cout << a;
            return 0;
        }
        else if (a[i] < b[i])
        {
            reverse(b.begin(), b.end());
            cout << b;
            return 0;
        }
    }

    return 0;
}