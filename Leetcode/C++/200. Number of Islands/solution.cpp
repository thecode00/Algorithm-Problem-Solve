// https://leetcode.com/problems/number-of-islands/

#include <vector>

using namespace std;

class Solution // DFS
{
public:
    int numIslands(vector<vector<char>> &grid)
    {
        int dx[4] = {0, 0, -1, 1}, dy[4] = {1, -1, 0, 0};
        int count = 0;
        for (int y = 0; y < grid.size(); y++)
        {
            for (int x = 0; x < grid[0].size(); x++)
            {
                if (grid[y][x] == '1')
                {
                    count += 1; // Count island
                    vector<pair<int, int>> stack;
                    stack.push_back({x, y});
                    grid[y][x] = '0'; // Check visit start point
                    while (!stack.empty())
                    {
                        int curX = stack.back().first, curY = stack.back().second;
                        stack.pop_back();
                        for (int idx = 0; idx < 4; idx++)
                        {
                            int newX = curX + dx[idx], newY = curY + dy[idx];
                            if (0 <= newX && newX < grid[0].size() && 0 <= newY && newY < grid.size() && grid[newY][newX] == '1')
                            {
                                grid[newY][newX] = '0';
                                stack.push_back({newX, newY});
                            }
                        }
                    }
                }
            }
        }

        return count;
    }
};