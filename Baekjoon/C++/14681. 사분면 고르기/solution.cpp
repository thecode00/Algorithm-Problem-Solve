// https://www.acmicpc.net/problem/14681

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int x, y;
    cin >> x >> y;
    if (x > 0 & y > 0)
        cout << 1;
    else if (x > 0 & y < 0)
        cout << 4;
    else if (x<0 & y> 0)
        cout << 2;
    else
        cout << 3;
}
