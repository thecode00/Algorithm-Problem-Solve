// https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/cpp

#include <string>
#include <vector>

bool check(const std::vector<std::string> &seq, const std::string &elem)
{
    for (std::string s : seq)
    {
        if (s == elem)
        {
            return true;
        }
    }
    return false;
}