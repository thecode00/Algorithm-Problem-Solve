// https://cses.fi/problemset/task/1647

#include <algorithm>
#include <iostream>
#include <climits>
#include <vector>

class SegmentTree
{
private:
    std::vector<int> _arr;
    std::vector<int> _tree;

public:
    SegmentTree(std::vector<int> &arr)
    {
        _arr = arr;
        _tree.assign(arr.size() * 4, INT_MAX);
    }

    void build(int node, int left, int right)
    {
        if (left == right)
        {
            _tree[node] = _arr[left];
        }
        else
        {
            int mid = left + (right - left) / 2; // Prevent overflow
            // build child node
            build(node * 2, left, mid);
            build(node * 2 + 1, mid + 1, right);
            // When root node is 1, node * 2 = left childe, hode * 2 + 1 = right child
            _tree[node] = std::min(_tree[node * 2], _tree[node * 2 + 1]);
        }
    }

    int query(int node, int left, int right, int start, int end)
    {
        if (end < left || right < start) // Not query range
        {
            return INT_MAX;
        }
        else if (start <= left && right <= end)
        {
            return _tree[node];
        }
        else
        {
            int mid = left + (right - left) / 2;
            // Return min num left, right child
            return std::min(query(node * 2, left, mid, start, end), query(node * 2 + 1, mid + 1, right, start, end));
        }
    }
};

int main(int argc, char const *argv[])
{
    int n, q; // Length of array, number of queries
    std::cin >> n >> q;

    std::vector<int> arr;
    for (int i = 0; i < n; i++)
    {
        int input;
        std::cin >> input;
        arr.push_back(input);
    }

    SegmentTree *tree = new SegmentTree(arr);
    int a, b, length = arr.size() - 1;
    tree->build(1, 0, length);
    for (int i = 0; i < q; i++)
    {
        std::cin >> a >> b;
        std::cout << tree->query(1, 0, length, a - 1, b - 1) << "\n";
    }
}
