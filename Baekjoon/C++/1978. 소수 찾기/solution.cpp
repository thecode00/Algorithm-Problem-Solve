// https://www.acmicpc.net/problem/1978

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int n;
    int total = 0;
    int enter;
    int primes[1001] = { false };
    cin >> n;

    for (int i = 2; i < 1001; i++) // 에스토라테너스의 체
    {
        int temp = i * 2;
        while (temp < 1001)
        {
            primes[temp] = true;
            temp += i;
        }
    }

    for (int i = 0; i < n; i++)
    {
        cin >> enter;
        if (!primes[enter] & enter > 1)
        {
            total += 1;
        }
    }

    cout << total;
    return 0;
}
