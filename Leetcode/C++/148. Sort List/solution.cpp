// https://leetcode.com/problems/sort-list/description/

#include <algorithm>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution // Merge sort
{
public:
    ListNode *sortList(ListNode *head)
    {
        if (!head || !head->next)
        {
            return head;
        }
        ListNode *prev = NULL, *slow = head, *fast = head;
        ListNode *temp;
        // Use runner for move slow to half
        while (fast && fast->next)
        {
            temp = slow;
            fast = fast->next->next;
            slow = slow->next;
            prev = temp;
        }
        prev->next = NULL; // Divide listnode
        ListNode *left = sortList(head), *right = sortList(slow);
        return merge(left, right);
    }

    ListNode *merge(ListNode *left, ListNode *right)
    {
        if (left && right)
        {
            if (left->val > right->val) // Always keep the left node as the smaller value
            {
                swap(left, right);
            }
            left->next = merge(left->next, right);
        }
        return left ? left : right;
    }
};