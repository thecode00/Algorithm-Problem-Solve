// https://cses.fi/problemset/task/1666/

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int parent[100001];

int find(int num) // Find parent city
{
    if (parent[num] != num)
    {
        parent[num] = find(parent[num]);
    }
    return parent[num];
}

void union_set(int a, int b) // Union two city
{
    a = find(a);
    b = find(b);
    if (a > b)
    {
        parent[a] = b;
    }
    else
    {
        parent[b] = a;
    }
}

int main()
{
    int cities, roads;
    cin >> cities >> roads;

    for (int i = 1; i <= cities; i++)
    {
        parent[i] = i;
    }

    for (int i = 0; i < roads; i++)
    {
        int a, b;
        cin >> a >> b;
        union_set(a, b);
    }

    set<int> need_connect;
    for (int i = 1; i <= cities; i++)
    {
        need_connect.insert(find(parent[i]));
    }

    cout << need_connect.size() - 1 << endl;
    if (need_connect.size() > 1)
    {
        auto it = need_connect.begin();
        int main = *it;
        ++it;
        while (it != need_connect.end())
        {
            cout << main << " " << *it << endl;
            ++it;
        }
    }

    return 0;
}
