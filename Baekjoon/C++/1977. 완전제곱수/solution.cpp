// https://www.acmicpc.net/problem/1977

#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int start, end;
    int sum = 0, square, min_square; // sum 초기화 잊지말기

    cin >> start >> end;

    square = ceil(sqrt(start)); // 시작값의 제곱근을 올림처리해서 완전제곱수의 범위를 현재값 이상으로 나오게 설정
    min_square = square;

    while (square * square <= end)
    {
        sum += square * square;
        square += 1;
    }

    if (sum == 0)
    {
        cout << -1;
    }
    else
    {
        cout << sum << "\n"
             << min_square * min_square;
    }

    return 0;
}
