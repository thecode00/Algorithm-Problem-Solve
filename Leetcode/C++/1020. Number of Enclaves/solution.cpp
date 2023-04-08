// https://leetcode.com/problems/number-of-enclaves/description/

#include <vector>

using namespace std;

class Solution
{
public:
    int numEnclaves(vector<vector<int>> &grid)
    {
        vector<int> dx = { 0, 0, 1, -1 }, dy = { 1, -1, 0, 0 };
        int area = 0;

        for (int y = 0; y < grid.size(); y++)
        {
            for (int x = 0; x < grid[0].size(); x++)
            {
                if (grid[y][x] == 1)
                {
                    int count = 1;
                    bool enclose = true;
                    vector<pair<int, int>> stack = { { y, x } };
                    grid[y][x] = 0;
                    while (!stack.empty())
                    { // DFS
                        int cur_y = stack.back().first, cur_x = stack.back().second;
                        stack.pop_back();

                        for (int idx = 0; idx < dx.size(); idx++)
                        {
                            int ny = cur_y + dy[idx], nx = cur_x + dx[idx];
                            if (ny < 0 || ny >= grid.size() || nx < 0 || nx >= grid[0].size())
                            {
                                enclose = false;
                                continue;
                            }
                            if (grid[ny][nx] == 1)
                            {
                                stack.push_back({ ny, nx });
                                grid[ny][nx] = 0;
                                count += 1;
                            }
                        }
                    }
                    if (enclose)
                    { // Add to area if enclosed
                        area += count;
                    }
                }
            }
        }
        return area;
    }
};