// https://leetcode.com/problems/queue-reconstruction-by-height/

// TODO: SOlve with priority_queue

#include <queue>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>> &people)
    {
        // For people in descending order of their height sort vector, if heights are equal, person with a smaller value of k appears first
        sort(people.begin(), people.end(), [](vector<int> &vec1, vector<int> &vec2)
             { if (vec1[0] == vec2[0]) return vec1[1] < vec2[1]; 
             return vec1[0] > vec2[0]; });

        vector<vector<int>> result;
        for (int i = 0; i < people.size(); i++)
        {
            vector<int> &person = people[i];
            int index = person[1];
            if (index >= result.size())
            {
                result.push_back(person);
            }
            else
            {
                result.insert(result.begin() + index, person);
            }
        }
        return result;
    }
};

class Solution
{
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>> &people)
    {
        priority_queue<vector<int>> pq;
        for (auto &vec : people)
        {
            pq.push(vec);
        }

        vector<vector<int>> result;
        for (int i = 0; i < people.size(); i++)
        {
            vector<int> &person = people[i];
            int index = person[1];
            if (index >= result.size())
            {
                result.push_back(person);
            }
            else
            {
                result.insert(result.begin() + index, person);
            }
        }
        return result;
    }
};