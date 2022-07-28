// https://www.acmicpc.net/problem/2744

#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main(int argc, char const *argv[])
{
    string str;
    getline(cin, str);
    for (int i = 0; i < str.size(); i++)
    {
        if (islower(str[i]))
        {
            str[i] = toupper(str[i]);
        }
        else
        {
            str[i] = tolower(str[i]);
        }
    }
    cout << str;
}
