// https://www.acmicpc.net/problem/4796

#include <algorithm>
#include <iostream>

int main(int argc, char const *argv[])
{
    std::cin.tie(0);
    std::cout.tie(0);

    int L, P, V, q, r, index = 1;
    while (true)
    {
        std::cin >> L >> P >> V;
        if (L == 0 && P == 0 && V == 0)
        {
            break;
        }
        // (휴가에 들어갈수있는 연속일수 * 연속일수중 캠핑장을 사용가능한 일수) + 남은 일수중 최대한 캠핑장을 사용가능한 일수를 넣음
        q = V / P;
        r = V % P;
        std::cout << "Case " << index << ": " << q * L + std::min(r, L) << "\n";
        index += 1;
    }
    return 0;
}
