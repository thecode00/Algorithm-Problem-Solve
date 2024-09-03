// https://leetcode.com/problems/convert-1d-array-into-2d-array/description

class Solution
{
public:
    vector<vector<int>> construct2DArray(vector<int> &original, int m, int n)
    {
        if (original.size() != (m * n))
        {
            return {};
        }
        vector<vector<int>> result(m, vector<int>());

        for (int y = 0; y < m; y++)
        {
            for (int x = 0; x < n; x++)
            {
                result[y].emplace_back(original[(n * y) + x]);
            }
        }

        return result;
    }
};

class Solution
{
public:
    vector<vector<int>> construct2DArray(vector<int> &original, int m, int n)
    {
        if (original.size() != (m * n))
        {
            return {};
        }
        vector<vector<int>> result;

        for (int y = 0; y < m * n;)
        {
            vector<int> temp;
            for (int x = 0; x < n; x++)
            {
                temp.emplace_back(original[y++]);
            }
            result.emplace_back(temp);
        }

        return result;
    }
};