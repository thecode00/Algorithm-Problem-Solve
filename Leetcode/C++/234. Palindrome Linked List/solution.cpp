// https://leetcode.com/problems/palindrome-linked-list/

#include <vector>

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
    bool isPalindrome(ListNode *head)
    {
        vector<int> listNode;
        // Move linkedList to vector
        while (head)
        {
            listNode.push_back(head->val);
            head = head->next;
        }

        int left = 0, right = listNode.size() - 1;
        // Check palindrome
        while (left < right)
        {
            if (listNode[left] != listNode[right])
            {
                return false;
            }
            left += 1;
            right -= 1;
        }
        return true;
    }
};

class Solution
{
public:
    bool isPalindrome(ListNode *head)
    {
        ListNode *slow = head, *fast = head, *reverse = NULL, *temp = head;
        while (fast && fast->next) // Move slow and reverse to center
        {
            fast = fast->next->next;
            temp = slow;
            slow = slow->next;
            temp->next = reverse;
            reverse = temp;
        }
        if (fast) // If fast is not NULL ListNode length is odd so move slow to next node
        {
            slow = slow->next;
        }
        while (slow) // Check palindrome
        {
            if (slow->val != reverse->val)
            {
                return false;
            }
            slow = slow->next;
            reverse = reverse->next;
        }
        return true;
    }
};