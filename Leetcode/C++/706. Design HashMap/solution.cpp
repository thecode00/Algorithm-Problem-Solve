// https://leetcode.com/problems/design-hashmap/
// Ref: https://leetcode.com/problems/design-hashmap/solutions/161483/c-solution-using-vector-of-lists/

#include <vector>

using namespace std;

class MyHashMap
{
public:
    vector<vector<pair<int, int>>> hashMap;
    int mapSize = 1000;
    MyHashMap()
    {
        hashMap.resize(mapSize);
    }

    void put(int key, int value)
    {
        int index = key % mapSize;
        for (auto &p : hashMap[index])
        {
            if (p.first == key)
            {
                p.second = value;
                return;
            }
        }
        hashMap[index].emplace_back(make_pair(key, value));
    }

    int get(int key)
    {
        int index = key % mapSize;
        for (auto &p : hashMap[index])
        {
            if (p.first == key)
            {
                return p.second;
            }
        }
        return -1;
    }

    void remove(int key)
    {
        int index = key % mapSize;
        for (int i = 0; i < hashMap[index].size(); i++)
        {
            if (hashMap[index][i].first == key)
            {
                hashMap[index].erase(hashMap[index].begin() + i);
                return;
            }
        }
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */