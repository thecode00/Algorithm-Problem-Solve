// https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/cpp

#include <cmath>

using namespace std;

long int findNextSquare(long int sq)
{
    long int sqrtSq = floor(sqrt(sq));
    if (sq % sqrtSq != 0)
    {
        return -1;
    }
    sqrtSq += 1;
    return sqrtSq * sqrtSq;
}