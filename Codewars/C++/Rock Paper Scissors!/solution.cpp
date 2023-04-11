// https://www.codewars.com/kata/5672a98bdbdd995fad00000f/train/cpp

#include <string>
#include <unordered_map>

std::string rps(const std::string &p1, const std::string &p2)
{
    std::unordered_map<std::string, std::string> winMap = { { "rock", "scissors" },
                                                            { "scissors", "paper" },
                                                            { "paper", "rock" } };
    if (p1 == p2)
    {
        return "Draw!";
    }
    else if (winMap[p1] == p2)
    {
        return "Player 1 won!";
    }
    else
    {
        return "Player 2 won!";
    }
}