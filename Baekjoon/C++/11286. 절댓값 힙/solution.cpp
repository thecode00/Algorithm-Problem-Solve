// https://www.acmicpc.net/problem/11286

#include <iostream>
#include <vector>
#include <queue>
// 첫번째 코드
struct CompareAbs
{
    bool operator()(int num1, int num2)
    {
        if (std::abs(num1) == std::abs(num2)) // 절대값이 같을때 크기 오름차순
        {
            return num1 > num2;
        }
        return std::abs(num1) > std::abs(num2); // 절대값 크기 오름차순
    }
};

int main(int argc, char const *argv[])
{
    // 빠른 입출력
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int n, input;
    std::cin >> n;
    std::priority_queue<int, std::vector<int>, CompareAbs> pq;

    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        if (input == 0)
        {
            if (pq.empty()) // 우선순위 큐가 비어있으면 0출력
            {
                std::cout << 0 << "\n";
            }
            else
            {
                std::cout << pq.top() << "\n";
                pq.pop();
            }
        }
        else
        {
            pq.emplace(input);
        }
    }
    return 0;
}

// 두번째 코드
typedef std::pair<int, int> pii;

struct ComparePairs
{
    bool operator()(const std::pair<int, int> &p1, const std::pair<int, int> &p2) const
    {
        if (std::abs(p1.first) == std::abs(p2.first)) // 절대값이 같을 경우, 원소의 크기로 비교
        {

            return p1.second > p2.second; // 오름차순으로 정렬
        }
        return p1.first > p2.first; // 오름차순으로 정렬
    }
};

int main(int argc, char const *argv[])
{
    // 빠른 입출력
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int n, input;
    std::cin >> n;
    std::priority_queue<pii, std::vector<pii>, ComparePairs> pq;

    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        if (input == 0)
        {
            if (pq.empty()) // 우선순위 큐가 비어있으면 0출력
            {
                std::cout << 0 << "\n";
            }
            else
            {
                std::cout << pq.top().second << "\n";
                pq.pop();
            }
        }
        else
        {
            pq.emplace(std::abs(input), input);
        }
    }
    return 0;
}

// 세번째 코드
int main(int argc, char const *argv[])
{
    // 빠른 입출력
    std::cin.tie(NULL);
    std::cout.tie(NULL);

    int n, input;
    std::cin >> n;
    // 양수는 수가 작을수록 절대값도 작으므로 최소힙으로 사용, 음수는 수가 클수록 절대값도 커지므로 최대힙으로 사용
    // c++는 우선순위큐가 최대힙이므로 양수 우선순위큐는 부호를 바꿔서 최소힙으로 만듬
    std::priority_queue<int> positive, negative;

    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        if (input == 0)
        {
            if (!positive.empty())
            {
                if (!negative.empty()) // 양수, 음수힙에 둘다 값이 있을때
                {
                    if (-positive.top() < std::abs(negative.top()))
                    {
                        std::cout << -positive.top() << "\n";
                        positive.pop();
                    }
                    else // 절대값이 같을때 작은값을 출력해야하므로 음수 힙에 있는 값을 출력
                    {
                        std::cout << negative.top() << "\n";
                        negative.pop();
                    }
                }
                else // 음수힙이 비었을결우
                {
                    std::cout << -positive.top() << "\n";
                    positive.pop();
                }
            }
            else // 양수힙이 비었을경우
            {
                if (!negative.empty())
                {
                    std::cout << negative.top() << "\n";
                    negative.pop();
                }
                else // 두 힙이 모두 비었을경우
                {
                    std::cout << 0 << "\n";
                }
            }
        }
        else
        {
            if (input > 0)
            {
                // 최소힙으로 사용하기위해 부호를 바꿔줌 출력할때도 잊지말고 부호를 바꿔서 출력해야함
                positive.push(-input);
            }
            else
            {
                negative.push(input);
            }
        }
    }
    return 0;
}
