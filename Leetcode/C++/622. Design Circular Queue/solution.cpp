// https://leetcode.com/problems/design-circular-queue/
// Ref: https://leetcode.com/problems/design-circular-queue/solutions/1141876/js-python-java-c-simple-array-solution-w-explanation/?orderBy=most_votes

#include <vector>

using namespace std;

class MyCircularQueue
{
    int maxSize;
    int curSize = 0;
    int head = 0, tail = -1;
    vector<int> queue;

public:
    MyCircularQueue(int k)
    {
        maxSize = k;
        queue.resize(k);
    }

    bool enQueue(int value)
    {
        if (isFull())
        {
            return false;
        }
        tail = (tail + 1) % maxSize;
        queue[tail] = value;
        curSize += 1;
        return true;
    }

    bool deQueue()
    {
        if (isEmpty())
        {
            return false;
        }
        head = (head + 1) % maxSize;
        curSize -= 1;
        return true;
    }

    int Front()
    {
        return isEmpty() ? -1 : queue[head];
    }

    int Rear()
    {
        return isEmpty() ? -1 : queue[tail];
    }

    bool isEmpty()
    {
        if (curSize > 0)
        {
            return false;
        }
        return true;
    }

    bool isFull()
    {
        if (curSize == maxSize)
        {
            return true;
        }
        return false;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */