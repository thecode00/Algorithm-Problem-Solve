// https://cses.fi/problemset/task/1669

#include <iostream>
#include <vector>

std::vector<int> visited;
std::vector<std::vector<int>> graph;
bool dfs(int start);

int main(int argc, char const *argv[])
{
    int n, m;
    std::cin >> n >> m;

    graph.resize(n + 1);
    visited.resize(n + 1, -1);

    for (int i = 0; i < m; i++)
    {
        int a, b;
        std::cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    bool isCycle = false;
    for (int i = 1; i <= n; i++)
    {
        if (visited[i] == -1)
        {
            isCycle = dfs(i);
            if (isCycle) // If found cycle stop search
            {
                break;
            }
        }
    }
    if (!isCycle) // If not found cycle print IMPOSSIBLE
    {
        std::cout << "IMPOSSIBLE";
    }
    return 0;
}

bool dfs(int start)
{
    std::vector<std::pair<int, int>> stack;
    stack.push_back({start, -1});
    while (!stack.empty())
    {
        int cur = stack.back().first, before = stack.back().second;
        stack.pop_back();
        if (visited[cur] != -1) // Prevent already visit city
        {
            continue;
        }
        visited[cur] = before;
        for (auto next : graph[cur])
        {
            if (next == before)
            {
                continue;
            }

            if (visited[next] == -1)
            {
                stack.push_back({next, cur});
            }
            else // Found cycle print cycle path and return true
            {
                std::vector<int> path;
                path.push_back(next);
                while (next != cur)
                {
                    path.push_back(cur);
                    cur = visited[cur];
                }
                path.push_back(next);
                std::cout << path.size() << std::endl;
                for (auto city : path)
                {
                    std::cout << city << " ";
                }
                return true;
            }
        }
    }
    return false; // There is no cycle so return false
}