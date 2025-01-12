// https://www.acmicpc.net/problem/11729

#include <iostream>

using namespace std;

void hanoi(int n, int ori, int temp, int dest);

int main(int argc, char const *argv[])
{
    int n;
    cin >> n;

    cout << (1 << n) - 1 << "\n";
    hanoi(n, 1, 2, 3);

    return 0;
}

void hanoi(int n, int ori, int temp, int dest)
{
    if (n == 1)
    {
        cout << ori << " " << dest << "\n";
        return;
    }

    hanoi(n - 1, ori, dest, temp);
    cout << ori << " " << dest << "\n";
    hanoi(n - 1, temp, ori, dest);
}