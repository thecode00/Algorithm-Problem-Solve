// https://www.acmicpc.net/problem/10844

#include <algorithm>
#include <iostream>

const int mod = 1000000000;

int main(int argc, char const *argv[])
{
    // 현재 길이가 n일때 cache의 0번째 리스트는 길이가 n - 1인 계단수의 개수들을 1번째 리스트는 길이가 n인 계단수의 개수들을 가지고있음
    // cache[1][3]은 길이가 n이고 끝자리가 3으로 끝나는 계단수의 수
    int cache[2][10]{};
    for (int i = 1; i < 10; i++)
    {
        cache[1][i] = 1;
    }
    int n;
    std::cin >> n;

    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            std::swap(cache[0][j], cache[1][j]);
            cache[1][j] = 0;
            // cache[0][j] = cache[1][j];
            // cache[1][j] = 0;
        }

        for (int k = 0; k < 10; k++)
        {
            if (k > 0)
            {
                cache[1][k] = (cache[1][k] + cache[0][k - 1]) % mod;
            }
            if (k < 9)
            {
                cache[1][k] = (cache[1][k] + cache[0][k + 1]) % mod;
            }
        }
    }

    int total = 0;
    for (auto num : cache[1])
    {
        total = (total + num) % mod;
    }

    std::cout << total;
    return 0;
}
