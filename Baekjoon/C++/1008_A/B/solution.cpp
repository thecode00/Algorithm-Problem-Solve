// https://www.acmicpc.net/problem/1008

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    double a, b;
    cin >> a >> b;
    cout.precision(20); // 소수점 자리수 조절
    cout << a / b;
    return 0;
}