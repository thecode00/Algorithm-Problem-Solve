// https://leetcode.com/problems/can-place-flowers/

#include <cstdlib>
#include <vector>

using namespace std;

class Solution
{
public:
    bool canPlaceFlowers(vector<int> &flowerbed, int n)
    {
        div_t divResult = div(flowerbed.size(), 2);
        if (n == 0)
        {
            return true;
        }
        else if (n > divResult.quot + divResult.rem)
        {
            return false;
        }

        for (int idx = 0; idx < flowerbed.size(); idx++)
        {
            // If idx == 0 cant search idx - 1 and if idx == len(flowerbed) - 1 index is last of flowerbed so cant search idx + 1
            if (flowerbed[idx] == 0 && (idx == 0 || flowerbed[idx - 1] == 0) && (idx == flowerbed.size() - 1 || flowerbed[idx + 1] == 0))
            {
                flowerbed[idx] = 1; // Plant flower
                n -= 1;
                if (n == 0)
                { // If plant all flower return true
                    return true;
                }
            }
        }
        return false;
    }
};