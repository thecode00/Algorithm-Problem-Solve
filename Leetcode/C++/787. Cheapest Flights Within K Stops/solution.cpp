// https://leetcode.com/problems/cheapest-flights-within-k-stops/

#include <vector>
#include <climits>
#include <queue>

using namespace std;

class Solution
{
public:
    int findCheapestPrice(int n, vector<vector<int>> &flights, int src, int dst, int k)
    {
        vector<int> distances(n, INT_MAX);
        vector<vector<pair<int, int>>> graph(n);
        for (vector<int> vec : flights)
        {
            int from = vec[0], to = vec[1], price = vec[2];
            graph[from].push_back({price, to});
        }

        priority_queue<tuple<int, int, int>> pq;
        pq.push({0, src, 0}); // distance, city, stops
        int newDist, nextCity;
        while (!pq.empty())
        {
            int dist = get<0>(pq.top()), city = get<1>(pq.top()), stops = get<2>(pq.top());
            pq.pop();
            if (distances[city] > dist)
            {
                distances[city] = dist;
                for (auto p : graph[city])
                {
                    newDist = dist + p.first;
                    nextCity = p.second;
                    // If distances[nextCity] is bigger than newDist and nextcity <= k stops push to priority_queue for search
                    if (distances[nextCity] > newDist && stops <= k)
                    {
                        pq.push({newDist, nextCity, stops + 1});
                    }
                }
            }
        }

        return distances[dst] == INT_MAX ? -1 : distances[dst];
    }
};