// https://leetcode.com/problems/reverse-linked-list-ii/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution
{
public:
    ListNode *reverseBetween(ListNode *head, int left, int right)
    {
        ListNode *root = new ListNode(0);
        ListNode *start = root;
        root->next = head;
        // During the swap, the values of start and end remain unchanged.
        for (int i = 0; i < left - 1; i++)
        {
            start = start->next;
        }
        ListNode *end = start->next;
        for (int i = 0; i < right - left; i++)
        {
            ListNode *temp = start->next;
            start->next = end->next;
            end->next = end->next->next;
            start->next->next = temp;
        }
        // The head node can be included in the range, so we create a dummy node and return its next pointer
        return root->next;
    }
};