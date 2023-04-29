// https://cses.fi/problemset/task/1668

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n, m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> friendShip(n + 1);
    for (int i = 0; i < m; i++)
    {
        int a, b;
        std::cin >> a >> b;
        friendShip[a].push_back(b);
        friendShip[b].push_back(a);
    }

    std::vector<int> team(n + 1, -1);
    bool isImpossible = false;
    for (int i = 1; i < n + 1; i++)
    {
        if (team[i] == -1)
        {
            // 0 = team1, 1 = team2
            team[i] = 0;
            std::vector<int> stack;
            stack.push_back(i);
            while (!stack.empty())
            {
                int cur = stack.back();
                stack.pop_back();
                for (int next : friendShip[cur])
                {
                    if (team[next] == -1)
                    {
                        // 1 XOR 1 = 0, 0 XOR 1 = 1
                        team[next] = team[cur] ^ 1;
                        stack.push_back(next);
                    }
                    else if (team[next] == team[cur])
                    {
                        isImpossible = true; // If Adjacent friend is same team there is no solution
                        break;
                    }
                }
            }
        }
    }

    if (isImpossible)
    {
        std::cout << "IMPOSSIBLE";
    }
    else
    {
        for (int idx = 1; idx < n + 1; idx++)
        {
            std::cout << team[idx] + 1 << " ";
        }
    }
    return 0;
}
