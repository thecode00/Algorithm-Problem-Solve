// https://www.acmicpc.net/problem/2178

#include <iostream>
#include <vector>
#include <string>
#include <queue>

// 4방향으로 움직이는 배열
const int dy[4] = {0, 0, 1, -1};
const int dx[4] = {1, -1, 0, 0};

int main(int argc, char const *argv[])
{
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> distance(n, std::vector<int>(m, 0));
    std::vector<std::vector<char>> maze(n);
    std::string input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        for (auto c : input)
        {
            maze[i].push_back(c);
        }
    }
    // BFS
    std::queue<std::pair<int, int>> q;
    // 시작지점 설정
    q.emplace(0, 0);
    distance[0][0] = 1;
    std::pair<int, int> cur;
    int x, y, newX, newY;
    while (!q.empty())
    {
        cur = q.front();
        x = cur.first;
        y = cur.second;
        q.pop();
        for (int idx = 0; idx < 4; idx++)
        {
            newX = x + dx[idx];
            newY = y + dy[idx];
            // 좌표가 미로를 벗어나지않고 벽도 아니고 한번도 방문하지 않은 좌표라면 큐에 좌표를 넣음
            if (0 <= newX && newX < m && 0 <= newY && newY < n && maze[newY][newX] == '1' && distance[newY][newX] == 0)
            {
                q.emplace(newX, newY);
                distance[newY][newX] = distance[y][x] + 1;
            }
        }
    }

    std::cout << distance[n - 1][m - 1];
    return 0;
}
