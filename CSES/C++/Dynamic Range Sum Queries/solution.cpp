// https://cses.fi/problemset/task/1648

#include <iostream>
#include <vector>

class SegmentTree
{
private:
    std::vector<long long> _arr;
    std::vector<long long> _tree;

public:
    SegmentTree(std::vector<long long> &arr)
    {
        _arr = arr;
        _tree.assign(arr.size() * 4, 0);
    }
    /*
    @param node: Index of segmentTree, root node start from 1 for easier calculations
    @param left, right: The range currently covered by the node
    */
    void build(int node, int left, int right)
    {
        if (left == right)
        {
            _tree[node] = _arr[left];
        }
        else
        {
            int mid = left + (right - left) / 2;
            build(node * 2, left, mid);
            build(node * 2 + 1, mid + 1, right);
            _tree[node] = _tree[node * 2] + _tree[node * 2 + 1];
        }
    }

    /*
    @param node: Index of segmentTree, root node start from 1 for easier calculations
    @param left, right: The range currently covered by the node
    @param start, end: The range where we want the value
    */
    long long query(int node, int left, int right, int start, int end)
    {
        if (start <= left && right <= end)
        {
            return _tree[node];
        }
        if (end < left || right < start) // Not query range
        {
            return 0;
        }
        int mid = left + (right - left) / 2;
        long long leftQuery = query(node * 2, left, mid, start, end);
        long long rightQuery = query(node * 2 + 1, mid + 1, right, start, end);
        return leftQuery + rightQuery;
    }

    /*
    @param node: Index of segmentTree, root node start from 1 for easier calculations
    @param change: New value of array[changeIndex]
    @param changeIndex: The index to modify the value
    @param left, right: The range currently covered by the node
    */
    void update(int node, long long change, int changeIndex, int left, int right)
    {
        if (left == right)
        {
            _tree[node] = change;
        }
        else
        {
            int mid = left + (right - left) / 2;
            // IMPORTANT!! not changeIndex <= right
            if (left <= changeIndex && changeIndex <= mid)
            {
                update(node * 2, change, changeIndex, left, mid);
            }
            else
            {
                update(node * 2 + 1, change, changeIndex, mid + 1, right);
            }
            _tree[node] = _tree[node * 2] + _tree[node * 2 + 1];
        }
    }
};

int main(int argc, char const *argv[])
{
    // Fast input, output
    std::ios::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);

    int n, q;
    std::cin >> n >> q;
    std::vector<long long> nums;

    long long input;
    for (int i = 0; i < n; i++)
    {
        std::cin >> input;
        nums.emplace_back(input);
    }
    // Build segmenttree
    SegmentTree *tree = new SegmentTree(nums);
    tree->build(1, 0, nums.size() - 1);

    int cmd, a, b;
    for (int i = 0; i < q; i++)
    {
        std::cin >> cmd >> a >> b;
        if (cmd == 2)
        {
            std::cout << tree->query(1, 0, nums.size() - 1, a - 1, b - 1) << "\n";
        }
        else
        {
            tree->update(1, b, a - 1, 0, nums.size() - 1);
        }
    }

    return 0;
}
