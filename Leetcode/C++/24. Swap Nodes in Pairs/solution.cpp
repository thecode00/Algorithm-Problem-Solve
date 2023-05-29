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
        ListNode *prev = new ListNode(0), *temp;
        ListNode *answer = prev;
        prev->next = head;
        while (head && head->next)
        {
            ListNode *next = head->next;
            prev->next = next;
            temp = head;
            head = next->next;
            next->next = temp;
            temp->next = head;
            prev = prev->next->next;
        }
        // answer node is dummy so return answer->next
        return answer->next;
    }
};