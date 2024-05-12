// https://codeforces.com/problemset/problem/4/A

#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
    int weight;

    cin >> weight;

    if ((weight % 2 != 0) || (weight <= 2))
    {
        cout << "NO";
        return 0;
    }

    cout << "YES";
    return 0;
}
