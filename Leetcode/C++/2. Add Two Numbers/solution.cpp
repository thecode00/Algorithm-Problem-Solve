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
class Solution // Recursion
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        return add(l1, l2, 0);
    }

    ListNode *add(ListNode *l1, ListNode *l2, int carry)
    {
        if (!l1 && !l2)
        {
            if (carry)
            {
                return new ListNode(carry);
            }
            return NULL;
        }
        int total = carry;
        ListNode *l1Next, *l2Next;

        if (!l1)
        {
            ListNode *temp = l1;
            l1 = l2;
            l2 = temp;
        }
        if (l1)
        {
            total += l1->val;
            l1Next = l1->next;
        }
        if (l2)
        {
            total += l2->val;
            l2Next = l2->next;
        }

        l1->val = total % 10;
        carry = (int)(total / 10);

        l1->next = add(l1Next, l2Next, carry);
        return l1;
    }
};