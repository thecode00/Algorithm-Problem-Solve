// https://leetcode.com/problems/minimum-height-trees/

#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

// Topological sort
class Solution // Optimized code
{
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges)
    {
        // Except one node
        if (n == 1)
        {
            return {0};
        }
        vector<vector<int>> graph(n);
        int a, b;
        vector<int> indegree(n, 0);
        // Make graph
        for (auto &edge : edges)
        {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
            indegree[edge[1]] += 1;
            indegree[edge[0]] += 1;
        }
        // Insert leaf node
        queue<int> q;
        for (int idx = 0; idx < n; idx++)
        {
            if (graph[idx].size() == 1)
            {
                q.push(idx);
            }
        }
        vector<int> result;
        // Remove leaf node while find root of minimum height tree
        while (!q.empty())
        {
            int length = q.size();
            result.clear();
            for (int i = 0; i < length; i++)
            {
                int leaf = q.front();
                q.pop();
                result.push_back(leaf);
                for (auto &node : graph[leaf])
                {
                    indegree[node] -= 1;
                    if (indegree[node] == 1)
                    {
                        q.push(node);
                    }
                }
            }
        }
        return result;
    }
};

class Solution // First code
{
public:
    vector<int> findMinHeightTrees(int n, vector<vector<int>> &edges)
    {
        if (n < 2)
        {
            return {0};
        }
        unordered_map<int, set<int>> graph;
        int a, b;
        for (auto &edge : edges)
        {
            a = edge[0];
            b = edge[1];
            graph[a].insert(b);
            graph[b].insert(a);
        }

        queue<int> q;
        for (auto &p : graph)
        {
            if (p.second.size() == 1)
            {
                q.push(p.first);
            }
        }

        while (graph.size() > 2)
        {
            int length = q.size();
            for (int i = 0; i < length; i++)
            {
                int leaf = q.front();
                q.pop();
                for (auto &num : graph[leaf])
                {
                    graph[num].erase(leaf);
                    if (graph[num].size() == 1)
                    {
                        q.push(num);
                    }
                }
                graph.erase(leaf);
            }
        }

        vector<int> result;
        for (auto &p : graph)
        {
            result.push_back(p.first);
        }
        return result;
    }
};