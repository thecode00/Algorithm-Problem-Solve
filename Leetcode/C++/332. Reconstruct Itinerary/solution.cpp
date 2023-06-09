// https://leetcode.com/problems/reconstruct-itinerary/

#include <vector>
#include <algorithm>
#include <map>
#include <string>

using namespace std;

class Solution
{
public:
    vector<string> path;
    vector<string> findItinerary(vector<vector<string>> &tickets)
    {
        unordered_map<string, vector<string>> airports;
        // To check visit by using pop_back on a vector, sort it in bigger lexical order.
        sort(tickets.rbegin(), tickets.rend());
        for (auto ticket : tickets)
        {
            airports[ticket[0]].push_back(ticket[1]);
        }
        dfs(airports, "JFK");
        // Airports are added to the path starting from the last airport, it needs to be reverse
        reverse(path.begin(), path.end());
        return path;
    }

    void dfs(unordered_map<string, vector<string>> &airports, string start)
    {
        while (!airports[start].empty())
        {
            string nextAirport = airports[start].back();
            airports[start].pop_back();
            // Visit smaller lexical order airport
            dfs(airports, nextAirport);
        }
        path.push_back(start);
    }
};