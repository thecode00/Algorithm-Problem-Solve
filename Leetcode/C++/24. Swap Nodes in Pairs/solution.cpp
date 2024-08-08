// https://leetcode.com/problems/swap-nodes-in-pairs/description/

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
    ListNode *swapPairs(ListNode *head)
    {
        ListNode *root = new ListNode(-1, head);
        ListNode *prev = root;

        while (head && head->next)
        {
            ListNode *nextNode = head->next->next;
            prev->next = head->next;
            head->next->next = head;
            head->next = nextNode;

            prev = head;
            head = head->next;
        }

        // root node is dummy so return root->next
        return root->next;
    }
};

class Solution
{
public:
    ListNode *swapPairs(ListNode *head)
    {
        // Recursion
        if (head && head->next)
        {
            ListNode *nextNode = head->next;

            head->next = swapPairs(nextNode->next);
            nextNode->next = head;
            return nextNode;
        }
        return head;
    }
};