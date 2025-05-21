// https://codeforces.com/problemset/problem/266/B

#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n, t;
    std::cin >> n >> t;

    std::vector<char> queue(n);

    for (int i = 0; i < n; i++)
    {
        std::cin >> queue[i];
    }

    for (int i = 0; i < t; i++)
    {
        int idx = 0;
        while (idx < n - 1)
        {
            if (queue[idx] == 'B' && queue[idx + 1] == 'G')
            {
                char temp = queue[idx];
                queue[idx] = queue[idx + 1];
                queue[idx + 1] = temp;
                idx += 1;
            }
            idx += 1;
        }
    }

    for (int i = 0; i < n; i++)
    {
        std::cout << queue[i];
    }
    std::cout << "\n";

    return 0;
}
