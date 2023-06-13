// https://leetcode.com/problems/course-schedule/
// Time complexity: O(N)

#include <vector>
#include <map>

using namespace std;

// Topological sort
class Solution
{
public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        vector<int> degree(numCourses, 0);
        map<int, vector<int>> graph;
        // create a graph and add indegree counts.
        for (vector<int> course : prerequisites)
        {
            int start = course[1], end = course[0];
            degree[end] += 1;
            graph[start].push_back(end);
        }
        // Find 0 indegree course
        vector<int> stack;
        for (int idx = 0; idx < numCourses; idx++)
        {
            if (degree[idx] == 0)
            {
                stack.push_back(idx);
            }
        }

        while (!stack.empty())
        {
            int course = stack.back();
            stack.pop_back();
            for (int next : graph[course])
            {
                degree[next] -= 1;
                // If course indegree become 0 add to stack
                if (degree[next] == 0)
                {
                    stack.push_back(next);
                }
            }
        }
        // If can't take course exist return false
        for (int n : degree)
        {
            if (n != 0)
            {
                return false;
            }
        }
        return true;
    }
};