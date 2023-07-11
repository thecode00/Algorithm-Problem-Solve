// https://leetcode.com/problems/network-delay-time/
// Time complexity: O((V + E)log V), V = number of vertex, E = number of edge

#include <vector>
#include <queue>
#include <climits>
#include <map>
#include <algorithm>

using namespace std;

class Solution // Runtime: 154ms
{
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k)
    {
        vector<vector<pair<int, int>>> graph(n + 1);
        for (auto &p : times) // Make graph
        {
            graph[p[0]].emplace_back(p[2], p[1]);
        }

        vector<int> distances(n + 1, INT_MAX);
        priority_queue<pair<int, int>> pq;
        // Start point
        distances[k] = 0;
        pq.emplace(0, k);
        int node, newDist;
        while (!pq.empty())
        {
            node = pq.top().second;
            pq.pop();
            for (auto &next : graph[node])
            {
                newDist = distances[node] + next.first;
                if (newDist < distances[next.second])
                {
                    pq.emplace(newDist, next.second);
                    distances[next.second] = newDist;
                }
            }
        }
        // graph is 1-index so start search index is distances.begin() + 1
        int maxDist = *max_element(distances.begin() + 1, distances.end());
        return maxDist == INT_MAX ? -1 : maxDist;
    }
};

class Solution // Runtime: 1375ms, maybe push_back() slow?
{
public:
    int networkDelayTime(vector<vector<int>> &times, int n, int k)
    {
        vector<vector<pair<int, int>>> graph(n + 1);
        for (auto &vec : times)
        {
            graph[vec[0]].push_back({vec[2], vec[1]});
        }

        vector<int> distances(n + 1, INT_MAX);
        distances[0] = 0;
        priority_queue<pair<int, int>> q;
        q.push({0, k});
        while (!q.empty())
        {
            int curWeight = q.top().first, curNode = q.top().second;
            q.pop();
            if (distances[curNode] > curWeight)
            {
                distances[curNode] = curWeight;
                for (auto &pair : graph[curNode])
                {
                    int w = pair.first + curWeight, n = pair.second;
                    if (distances[n] > w)
                    {
                        q.push({w, n});
                    }
                }
            }
        }

        int maxDist = 0;
        for (int d : distances)
        {
            maxDist = max(d, maxDist);
        }
        if (maxDist != INT_MAX)
        {
            return maxDist;
        }
        return -1;
    }
};
