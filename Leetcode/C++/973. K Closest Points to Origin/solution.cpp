// https://leetcode.com/problems/k-closest-points-to-origin/description/

#include <algorithm>
#include <vector>

using namespace std;

// Ref: https://leetcode.com/problems/k-closest-points-to-origin/solutions/217999/java-c-python-o-n/
class Solution
{
public:
    vector<vector<int>> kClosest(vector<vector<int>> &points, int k)
    {
        /*
        Sort with compare lambda function
        The comparison function establishes the sorting criterion.
        */
        nth_element(points.begin(), points.begin() + k, points.end(), [](vector<int> &v1, vector<int> &v2)
                    { return v1[0] * v1[0] + v1[1] * v1[1] < v2[0] * v2[0] + v2[1] * v2[1]; });
        return vector<vector<int>>(points.begin(), points.begin() + k);
    }
};