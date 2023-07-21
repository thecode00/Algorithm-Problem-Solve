// https://www.acmicpc.net/problem/2512

#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    std::cin.tie(0);
    std::cout.tie(0);

    int n;
    std::cin >> n;
    std::vector<int> needs(n);
    for (int i = 0; i < n; i++)
    {
        std::cin >> needs[i];
    }

    int maxBudget; // 예산총액
    std::cin >> maxBudget;

    int mid, total, left = 0, right = *max_element(needs.begin(), needs.end());
    while (left <= right)
    {
        mid = left + (right - left) / 2;
        total = 0;
        for (auto need : needs)
        {
            if (need <= mid)
            {
                total += need;
            }
            else
            {
                total += mid;
            }
        }

        if (total <= maxBudget)
        {
            left = mid + 1;
        }
        else
        {
            right = mid - 1;
        }
    }
    // left는 예산합이 예산총액보다 적거나 같은 상한액 + 1 이므로 -1을 해서 최대상한액을 출력
    std::cout << left - 1;
    return 0;
}
