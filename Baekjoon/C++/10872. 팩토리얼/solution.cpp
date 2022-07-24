// https://www.acmicpc.net/problem/10872

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int n, answer = 1;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        answer *= i;
    }
    cout << answer;
}
