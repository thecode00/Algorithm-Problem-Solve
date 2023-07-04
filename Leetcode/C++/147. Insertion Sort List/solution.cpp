// https://leetcode.com/problems/insertion-sort-list/

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *insertionSortList(ListNode *head)
    {
        ListNode *root = new ListNode();
        ListNode *cur = root, *temp;
        // head = root of not sorted listnodes
        while (head)
        {
            while (cur->next && cur->next->val < head->val) // Move to insert index
            {
                cur = cur->next;
            }
            temp = cur->next;
            cur->next = head;
            head = head->next;
            cur->next->next = temp;
            // Id head->val smaller than cur->val head cant come after cur index so return to root of sorted listnodes
            if (head && cur->val > head->val)
            {
                cur = root;
            }
        }
        return root->next;
    }
};