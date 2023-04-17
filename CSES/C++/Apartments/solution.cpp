// https://cses.fi/problemset/task/1084

#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    int n, m, k; // Number of applicants, Number of apartment, maximum different
    std::cin >> n >> m >> k;
    std::vector<int> applicants, apartment;
    for (int i = 0; i < n; i++)
    {
        int temp;
        std::cin >> temp;
        applicants.push_back(temp);
    }
    for (int i = 0; i < m; i++)
    {
        int temp;
        std::cin >> temp;
        apartment.push_back(temp);
    }

    sort(applicants.begin(), applicants.end());
    sort(apartment.begin(), apartment.end());

    int appIndex = 0, apartIndex = 0;
    int count = 0;
    while (appIndex < n && apartIndex < m)
    {
        if (abs(apartment[apartIndex] - applicants[appIndex]) <= k)
        {
            count += 1;
            apartIndex += 1;
            appIndex += 1;
        }
        else
        {
            if (apartment[apartIndex] - applicants[appIndex] > k) // When apart is bigger than applicant
            {
                appIndex += 1;
            }
            else // When applicant is bigger than apart
            {
                apartIndex += 1;
            }
        }
    }
    std::cout << count;
    return 0;
}
