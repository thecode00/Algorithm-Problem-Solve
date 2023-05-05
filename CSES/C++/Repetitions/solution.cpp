// https://cses.fi/problemset/task/1069

#include <iostream>
#include <string>

int main(int argc, char const *argv[])
{
    std::string dna;
    std::cin >> dna;
    char cur = '@';
    int length = 1, maxLength, end = dna.size() - 1;
    for (int idx = 0; idx < dna.size(); idx++)
    {
        if (dna[idx] != cur)
        {
            cur = dna[idx];
            maxLength = std::max(length, maxLength);
            length = 1; // Reset length
        }
        else
        {
            length += 1;
        }

        if (idx == end) // If index is end of dna compare current length and maxLength
        {
            maxLength = std::max(length, maxLength);
        }
    }
    std::cout << maxLength;
    return 0;
}
