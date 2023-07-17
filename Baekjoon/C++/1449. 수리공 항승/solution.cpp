// https://www.acmicpc.net/problem/1449

#include <algorithm>
#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n, l; // 구멍개수, 테이프 길이
    int tapes = 0;
    std::cin >> n >> l;

    std::vector<int> holes;
    int input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        holes.push_back(input);
    }
    std::sort(holes.begin(), holes.end());

    int index = 0, end;
    while (index < holes.size())
    {
        tapes += 1;
        end = holes[index] + l - 1; // 테이프가 커버할수있는 범위
        // 테이프가 커버하지 못한 구멍으로 이동
        while (index < holes.size() && holes[index] <= end)
        {
            index += 1;
        }
    }
    std::cout << tapes;
    return 0;
}
