// https://codeforces.com/problemset/problem/381/A

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;

    std::vector<int> cards(n);

    for (int idx = 0; idx < n; idx++)
    {
        std::cin >> cards[idx];
    }

    int left = 0;
    int right = n - 1;
    std::vector<int> scores = { 0, 0 };
    int turn = 0;

    while (left < right)
    {
        if (cards[left] < cards[right])
        {
            scores[turn] += cards[right];
            right -= 1;
        }
        else
        {
            scores[turn] += cards[left];
            left += 1;
        }

        turn ^= 1;

        if (cards[left] < cards[right])
        {
            scores[turn] += cards[right];
            right -= 1;
        }
        else
        {
            scores[turn] += cards[left];
            left += 1;
        }

        turn ^= 1;
    }

    if (left == right)
    {
        scores[turn] += cards[right];
    }

    for (int idx = 0; idx < scores.size(); idx++)
    {
        std::cout << scores[idx] << " ";
    }
    std::cout << "\n";
    return 0;
}
