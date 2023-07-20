// https://www.acmicpc.net/problem/11724

#include <iostream>
#include <vector>

void dfs(int start, std::vector<bool> &visited, std::vector<std::vector<int>> &graph)
{
    std::vector<int> stack;
    stack.emplace_back(start);
    visited[start] = true;
    int cur;
    while (!stack.empty())
    {
        cur = stack.back();
        stack.pop_back();

        for (auto next : graph[cur])
        {
            if (!visited[next])
            {
                visited[next] = true;
                stack.emplace_back(next);
            }
        }
    }
}

int main(int argc, char const *argv[])
{
    // 빠른 입출력
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int n, m; // 노드, 간선 개수
    std::cin >> n >> m;
    std::vector<std::vector<int>> graph(n + 1);
    std::vector<bool> visited(n + 1, false);
    int u, v;
    for (int i = 0; i < m; i++)
    {
        std::cin >> u >> v;
        // 무방향 그래프이므로 양쪽에 노드 추가
        graph[u].emplace_back(v);
        graph[v].emplace_back(u);
    }

    int component = 0;
    for (int i = 1; i <= n; i++)
    {
        if (!visited[i]) // 아직 방문하지 않은 연결요소 dfs로 방문
        {
            dfs(i, visited, graph);
            component += 1;
        }
    }

    std::cout << component;
    return 0;
}
