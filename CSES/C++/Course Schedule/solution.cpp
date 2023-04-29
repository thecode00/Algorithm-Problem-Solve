// https://cses.fi/problemset/task/1679

#include <iostream>
#include <vector>
#include <queue>

int main(int argc, char const *argv[]) // Topological Sort
{
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> graph(n + 1);
    std::vector<int> inDegree(n + 1, 0);
    for (int i = 0; i < m; i++)
    {
        int a, b;
        std::cin >> a >> b;
        graph[a].push_back(b);
        inDegree[b] += 1;
    }

    std::queue<int> q;
    std::vector<int> result;
    for (int i = 1; i < n + 1; i++)
    {
        if (inDegree[i] == 0)
        {
            q.push(i);
            result.push_back(i);
        }
    }

    while (!q.empty())
    {
        int cur = q.front();
        q.pop();
        for (int next : graph[cur])
        {
            inDegree[next] -= 1;
            if (inDegree[next] == 0)
            {
                q.push(next);
                result.push_back(next);
            }
        }
    }

    if (result.size() == n)
    {
        for (auto node : result)
        {
            std::cout << node << " ";
        }
    }
    else
    {
        std::cout << "IMPOSSIBLE";
    }
    return 0;
}
