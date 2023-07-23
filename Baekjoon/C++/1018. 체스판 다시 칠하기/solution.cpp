// https://www.acmicpc.net/problem/1018

#include <algorithm>
#include <climits>
#include <iostream>
#include <string>
#include <vector>

const char bw[2] = { 'B', 'W' };

int checkRow(int color, int startY, int startX, std::vector<std::vector<char>> &board)
{
    // @brief: 보드의 한줄을 검사하는 함수
    int total = 0;
    for (int x = startX; x < startX + 8; x++)
    {
        if (bw[color % 2] != board[startY][x])
        {
            total += 1;
        }
        color += 1; // 색 변경
    }
    return total;
}

int checkBoard(int color, int startY, int startX, std::vector<std::vector<char>> &board)
{
    // @brief: 보드를 검사하는 함수
    int total = 0;
    for (int y = startY; y < startY + 8; y++)
    {
        total += checkRow(color, y, startX, board);
        color += 1; // 색 변경
    }
    return total;
}

int main(int argc, char const *argv[])
{
    int n, m;
    std::cin >> n >> m;

    std::vector<std::vector<char>> board(n);
    std::string input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        for (auto c : input)
        {
            board[i].emplace_back(c);
        }
    }

    int minChange = INT_MAX;
    for (int y = 0; y < n - 7; y++)
    {
        for (int x = 0; x < m - 7; x++)
        {
            minChange = std::min(minChange, checkBoard(0, y, x, board)); // 첫번째 칸이 검은색인 보드 검사
            minChange = std::min(minChange, checkBoard(1, y, x, board)); // 첫번째 칸이 흰색인 보드 검사
        }
    }

    std::cout << minChange;
    return 0;
}
