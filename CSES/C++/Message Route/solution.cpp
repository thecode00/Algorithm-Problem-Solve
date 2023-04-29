// https://cses.fi/problemset/task/1667

#include <iostream>
#include <unordered_map>
#include <vector>
#include <queue>

int main(int argc, char const *argv[])
{
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> graph(n + 1); // Adjacency list
    std::unordered_map<int, int> path;
    path[1] = 1; // Start point

    for (int i = 0; i < m; i++)
    {
        int a, b;
        std::cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    std::queue<int> q;
    q.push(1);
    while (!q.empty()) // BFS
    {
        int cur = q.front();
        q.pop();
        for (auto next : graph[cur])
        {
            if (path.find(next) == path.end())
            {
                path[next] = cur;
                q.push(next);
            }
        }
    }

    if (path.find(n) == path.end()) // Not connected
    {
        std::cout << "IMPOSSIBLE";
    }
    else
    {
        std::vector<int> p;
        p.push_back(n);
        while (n != 1)
        {
            p.push_back(path[n]);
            n = path[n];
        }
        std::cout << p.size() << "\n";
        for (int i = p.size() - 1; i >= 0; i--)
        {
            std::cout << p[i] << " ";
        }
    }
    return 0;
}
