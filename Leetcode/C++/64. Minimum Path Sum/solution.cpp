// https://leetcode.com/problems/minimum-path-sum/description/
// Time complexity: O(N * M), N = grid.length, M = grid[0].length

#include <vector>

using namespace std;

class Solution
{
public:
    int minPathSum(vector<vector<int>> &grid)
    {
        int lenX = grid[0].size(), lenY = grid.size();

        for (int y = 0; y < lenY; y++)
        {
            for (int x = 0; x < lenX; x++)
            {
                if (y && x)
                {
                    grid[y][x] += min(grid[y - 1][x], grid[y][x - 1]);
                }
                else if (y) // If x == 0 move down
                {
                    grid[y][x] += grid[y - 1][x];
                }
                else if (x) // If y == 0 move right
                {
                    grid[y][x] += grid[y][x - 1];
                }
            }
        }
        return grid[lenY - 1][lenX - 1];
    }
};