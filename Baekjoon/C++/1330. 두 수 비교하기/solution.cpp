// https://www.acmicpc.net/problem/1330

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int a, b;
    cin >> a >> b;
    if (a > b)
        cout << ">";
    else if (a == b)
        cout << "==";
    else
        cout << "<";
}
