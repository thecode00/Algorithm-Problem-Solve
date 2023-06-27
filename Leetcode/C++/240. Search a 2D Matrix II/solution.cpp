// https://leetcode.com/problems/search-a-2d-matrix-ii/description/

#include <vector>
#include <algorithm>

using namespace std;

class Solution // First code, binary search each row: O(n log n)
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        for (auto &row : matrix)
        {
            auto idx = lower_bound(row.begin(), row.end(), target);
            if (idx != row.end() && *idx == target)
            {
                return true;
            }
        }
        return false;
    }
};

class Solution
{
public:
    bool searchMatrix(vector<vector<int>> &matrix, int target)
    {
        int row = 0, col = matrix[0].size() - 1;
        while (row < matrix.size() && col >= 0)
        {
            if (matrix[row][col] > target)
            {
                col--;
            }
            else if (matrix[row][col] < target)
            {
                row++;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
};