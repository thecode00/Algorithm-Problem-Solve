// https://codeforces.com/problemset/problem/750/A

#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, k, time = 240, solved = 0;

    cin >> n >> k;
    time -= k;

    for (int i = 1; i <= n; i++)
    {
        if (time - (i * 5) < 0)
        {
            break;
        }

        solved++;
        time -= (i * 5);
    }

    cout << solved << endl;
    return 0;
}
