// https://leetcode.com/problems/merge-k-sorted-lists/description/

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

#include <algorithm>
#include <queue>

using namespace std;

class Solution
{
public:
    ListNode *mergeKLists(vector<ListNode *> &lists)
    {
        ListNode *root = new ListNode(0);
        ListNode *head = root;
        priority_queue<pair<int, ListNode *>> q;
        for (auto l : lists)
        {
            if (l == NULL)
            {
                continue;
            }
            // priority_queue is sorted in descending order by default
            // So multiple -1 make for ascending order
            q.push(make_pair(l->val * -1, l));
        }

        while (!q.empty())
        {
            ListNode *cur = q.top().second;
            q.pop();
            if (cur->next != NULL)
            {
                q.push(make_pair(cur->next->val * -1, cur->next));
            }
            // Cut node
            cur->next = NULL;
            // Merge node
            head->next = cur;
            head = head->next;
        }
        return root->next;
    }
};