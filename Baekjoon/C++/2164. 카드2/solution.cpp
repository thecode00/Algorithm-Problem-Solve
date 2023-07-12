// https://www.acmicpc.net/problem/2164

#include <iostream>
#include <queue>

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;
    std::queue<int> cards;
    for (int i = 1; i <= n; i++)
    {
        cards.emplace(i);
    }
    while (cards.size() > 1)
    {
        // 맨 위의 카드를 버림
        cards.pop();
        // 맨 위의 카드를 맨 아래로 보냄
        cards.emplace(cards.front());
        cards.pop();
    }
    std::cout << cards.front();
    return 0;
}
