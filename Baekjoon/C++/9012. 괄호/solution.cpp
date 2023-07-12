// https://www.acmicpc.net/problem/9012

#include <vector>
#include <iostream>
#include <string>

bool check(std::string &ps)
{
    std::vector<char> stack;
    for (auto s : ps)
    {
        if (s == ')')
        {
            // 닫는 괄호가 나왔는데 여는 괄호가 없다면 올바른 괄호가 아님 ex. ())
            if (stack.empty())
            {
                return false;
            }
            stack.pop_back();
        }
        else
        {
            stack.emplace_back('(');
        }
    }
    // 문자열의 모든 닫는괄호를 사용했는데 여는괄호가 남아있는경우 올바른 괄호가 아님 ex. ()(
    return stack.empty() ? true : false;
}

int main(int argc, char const *argv[])
{
    int n;
    std::cin >> n;
    std::string input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        std::cout << (check(input) ? "YES" : "NO") << "\n";
    }
    return 0;
}
