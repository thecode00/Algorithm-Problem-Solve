// https://www.acmicpc.net/problem/11726

#include <iostream>
#include <vector>

int main(int argc, char const *argv[]) // 타뷸레이션
{
    std::cin.tie(0);
    std::cout.tie(0);

    int n;
    std::cin >> n;
    if (n <= 2)
    {
        std::cout << n;
        return 0;
    }
    std::vector<int> cache(n + 1);
    cache[1] = 1;
    cache[2] = 2;

    for (int i = 3; i <= n; i++)
    {
        // 1x2 블록, 2x1블록을 추가한 조합을 더함
        cache[i] = (cache[i - 1] + cache[i - 2]) % 10007;
    }
    std::cout << cache[n];
    return 0;
}
