// https://leetcode.com/problems/add-two-numbers/

#include <cmath>

using namespace std;
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
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *result = new ListNode();
        ListNode *cur = result;
        int carry = 0;
        while (l1 || l2 || carry)
        {
            int total = 0;
            // Add numbers
            if (l1)
            {
                total += l1->val;
                l1 = l1->next;
            }
            if (l2)
            {
                total += l2->val;
                l2 = l2->next;
            }
            div_t divmod = div(total + carry, 10);
            ListNode *nextNode = new ListNode(divmod.rem);
            carry = divmod.quot;
            cur->next = nextNode;
            cur = nextNode;
        }
        // result is dummy node so return result->next
        return result->next;
    }
};