// https://cses.fi/problemset/task/1192

#include <iostream>
#include <vector>
#include <queue>

const int dy[4] = {0, 0, 1, -1};
const int dx[4] = {1, -1, 0, 0};

// Prototype
void bfs(int y, int x, std::vector<std::vector<char>> &board);

int main(int argc, char const *argv[])
{
    int width, height;
    int count = 0;
    std::cin >> height >> width;

    std::vector<std::vector<char>> board(height, std::vector<char>(width));
    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            std::cin >> board[y][x];
        }
    }

    for (int y = 0; y < height; y++)
    {
        for (int x = 0; x < width; x++)
        {
            if (board[y][x] == '.')
            { // Found room
                count += 1;
                bfs(y, x, board);
            }
        }
    }
    std::cout << count;
    return 0;
}

void bfs(int y, int x, std::vector<std::vector<char>> &board)
{
    board[y][x] = '#'; // Check visited
    std::queue<std::pair<int, int>> q;
    q.push(std::make_pair(y, x));

    while (!q.empty())
    {
        int curY = q.front().first, curX = q.front().second;
        q.pop();
        for (int idx = 0; idx < 4; idx++)
        {
            int newY = curY + dy[idx], newX = curX + dx[idx];
            if (0 <= newY && newY < board.size() && 0 <= newX && newX < board[0].size() && board[newY][newX] == '.')
            {
                q.push(std::make_pair(newY, newX));
                board[newY][newX] = '#'; // Check visited
            }
        }
    }
}