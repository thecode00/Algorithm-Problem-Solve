// https://leetcode.com/problems/task-scheduler/description/
// Ref: https://leetcode.com/problems/task-scheduler/solutions/104504/c-8lines-o-n/

#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution
{
public:
    int leastInterval(vector<char> &tasks, int n)
    {
        unordered_map<char, int> count;
        int most = 0;
        for (auto task : tasks)
        {
            count[task] += 1;
            most = max(most, count[task]);
        }
        // Calculate cycles length exclude last cycle
        // Why (n + 1)?: each cycle length = cooltime = n + compute most task 1
        // Ex. tasks = ["A", "A"], n = 2: A(1)##(n) - A
        int time = (most - 1) * (n + 1);

        for (auto p : count)
        {
            // Add last cycle
            if (p.second == most)
            {
                time += 1;
            }
        }
        // Ex. tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], n = 2
        // A##A##A -> AB#AB#AB -> ABCABCABC -> ABC(D)ABC(D)ABC -> ABCD(E)ABCDABC
        // We can insert every task end of most task cycle(ABC)
        return max((int)tasks.size(), time);
    }
};