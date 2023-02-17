// https://www.acmicpc.net/problem/2442

#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int blank, line;
    cin >> line;
    blank = line - 1;

    for (int i = 0; i < line; i++)
    {
        for (int j = 0; j < blank - i; j++)
        {
            cout << " ";
        }

        for (int j = 0; j < 2 * (i + 1) - 1; j++)
        {
            cout << "*";
        }
        cout << "\n";
    }

    return 0;
}
