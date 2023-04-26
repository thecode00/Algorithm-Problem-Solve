// https://cses.fi/problemset/task/1193

#include <iostream> // cin, cout
#include <string>
#include <queue>
#include <vector>    // vector, pair
#include <algorithm> // reverse

char board[1000][1000];
int previousMove[1000][1000];
const int dy[4] = {0, 0, 1, -1};
const int dx[4] = {1, -1, 0, 0};
const std::string move = "RLDU";

int main(int argc, char const *argv[])
{
    int height, width;
    int aY, aX;
    int bY, bX;
    std::cin >> height >> width;

    for (int y = 0; y < height; y++)
    {
        std::string s;
        std::cin >> s;
        for (int x = 0; x < width; x++)
        {
            if (s[x] == 'A') // Save 'A' position
            {
                aY = y;
                aX = x;
            }
            else if (s[x] == 'B')
            { // Save 'B' position
                bY = y;
                bX = x;
            }
            board[y][x] = s[x];
        }
    }

    std::queue<std::pair<int, int>> q;
    q.push(std::make_pair(aY, aX)); // Start point
    board[aY][aX] = '#';
    while (!q.empty()) // BFS
    {
        int curY = q.front().first;
        int curX = q.front().second;
        q.pop();
        for (int idx = 0; idx < 4; idx++)
        {
            int newY = curY + dy[idx], newX = curX + dx[idx];
            if (0 <= newY && newY < height && 0 <= newX && newX < width && (board[newY][newX] == '.' || board[newY][newX] == 'B'))
            {
                previousMove[newY][newX] = idx; // Save previous action
                board[newY][newX] = '#';
                q.push(std::make_pair(newY, newX));
            }
        }
    }

    if (board[bY][bX] == '#') // Reach 'B'
    {
        std::cout << "YES\n";
        std::vector<char> pathHistory;
        while (bY != aY || bX != aX)
        {
            int index = previousMove[bY][bX];
            pathHistory.push_back(move[index]);
            bY -= dy[index];
            bX -= dx[index];
        }
        std::cout << pathHistory.size() << "\n";
        std::reverse(pathHistory.begin(), pathHistory.end());
        for (auto c : pathHistory)
        {
            std::cout << c;
        }
    }
    else
    { // Cant reach 'B'
        std::cout << "NO";
    }
    return 0;
}
