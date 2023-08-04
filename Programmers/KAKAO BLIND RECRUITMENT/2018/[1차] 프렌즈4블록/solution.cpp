// https://school.programmers.co.kr/learn/courses/30/lessons/17679?language=cpp

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// @brief: 근처 4블록이 같은블록인지 확인하는 함수
bool checkPop(vector<vector<char>> &gameBoard, int y, int x)
{
    return gameBoard[y][x] == gameBoard[y][x + 1] && gameBoard[y][x] == gameBoard[y + 1][x + 1] && gameBoard[y][x] == gameBoard[y + 1][x];
}

int solution(int m, int n, vector<string> board)
{
    vector<vector<char>> gameBoard(m);
    // 게임 중간에 떨어지는걸 구현하기 위해 string벡터에서 변경이 가능한 char벡터로 변경
    for (int idx = 0; idx < m; idx++)
    {
        for (auto c : board[idx])
        {
            gameBoard[idx].emplace_back(c);
        }
    }

    while (true)
    {
        vector<pair<int, int>> popPoint;
        for (int y = 0; y < m - 1; y++)
        {
            for (int x = 0; x < n - 1; x++)
            {
                if (gameBoard[y][x] != '#' && checkPop(gameBoard, y, x))
                {
                    popPoint.emplace_back(x, y);
                }
            }
        }

        if (popPoint.size() == 0) //  더 이상 지울 블록이 없으므로 탐색 멈춤
        {
            break;
        }

        for (auto point : popPoint)
        {
            int popX = point.first, popY = point.second;
            gameBoard[popY][popX] = '#';
            gameBoard[popY + 1][popX] = '#';
            gameBoard[popY][popX + 1] = '#';
            gameBoard[popY + 1][popX + 1] = '#';
        }
        //  블록 내려가기 구현
        for (int i = 0; i < m - 2; i++) // 보드에서 내려야할 블록의 최대개수는 높이 - 맨밑에 생긴 구멍: m - 2
        {
            for (int y = 0; y < m - 1; y++)
            {
                for (int x = 0; x < n; x++)
                {
                    if (gameBoard[y + 1][x] == '#')
                    {
                        swap(gameBoard[y][x], gameBoard[y + 1][x]);
                    }
                }
            }
        }
    }
    // 빈칸 개수 세기
    int countBlank = 0;
    for (auto row : gameBoard)
    {
        countBlank += count(row.begin(), row.end(), '#');
    }
    return countBlank;
}