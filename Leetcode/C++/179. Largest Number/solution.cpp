// https://leetcode.com/problems/largest-number/description/

#include <algorithm>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class Solution // Optimized code
{
public:
    string largestNumber(vector<int> &nums)
    {
        vector<string> strNums;
        for (auto num : nums)
        {
            strNums.push_back(to_string(num));
        }
        // Using a lambda function for sorting
        sort(strNums.begin(), strNums.end(), [](string num1, string num2)
             { return num1 + num2 > num2 + num1; });

        string result = "";
        for (auto s : strNums)
        {
            result += s;
        }
        return result[0] == '0' ? "0" : result;
    }
};

class Solution // First code
{
public:
    string largestNumber(vector<int> &nums)
    {
        int sort_index = 1;
        while (sort_index < nums.size())
        {
            int index = sort_index;
            /*
            ex. nums[temp - 1] = 9, nums[temp] = 10
            Check 910 < 109
            If false not move numbers than continue
            */
            while (index > 0 && compare(to_string(nums[index - 1]), to_string(nums[index])))
            {
                swap(nums[index - 1], nums[index]);
                index--;
            }
            sort_index++;
        }
        // Move vector data to string
        stringstream ss;
        for (auto num : nums)
        {
            ss << to_string(num);
        }
        string result = ss.str();
        return result[0] == '0' ? "0" : result;
    }

    bool compare(string num1, string num2)
    {
        return num1 + num2 < num2 + num1;
    }
};
