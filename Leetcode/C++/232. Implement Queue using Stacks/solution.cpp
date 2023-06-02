// https://leetcode.com/problems/implement-queue-using-stacks/

#include <vector>

using namespace std;

class MyQueue
{
public:
    vector<int> stack_in;
    vector<int> stack_out;
    MyQueue()
    {
    }

    void push(int x)
    {
        stack_in.push_back(x);
    }

    int pop()
    {
        peek();
        int num = stack_out.back();
        stack_out.pop_back();
        return num;
    }

    int peek()
    {
        if (stack_out.empty())
        {
            while (!stack_in.empty())
            {
                int num = stack_in.back();
                stack_in.pop_back();
                stack_out.push_back(num);
            }
        }
        return stack_out.back();
    }

    bool empty()
    {
        return stack_out.empty() && stack_in.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */