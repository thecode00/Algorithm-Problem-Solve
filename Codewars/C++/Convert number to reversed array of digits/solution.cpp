// https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/cpp

#include <vector>

std::vector<int> digitize(unsigned long n)
{
    std::vector<int> result;
    if (!n)
    {
        result.push_back(0);
        return result;
    }
    while (n)
    {
        result.push_back(n % 10);
        n /= 10;
    }
    return result;
}