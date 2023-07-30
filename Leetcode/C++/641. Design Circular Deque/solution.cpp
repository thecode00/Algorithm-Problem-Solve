// https://leetcode.com/problems/design-circular-deque/
// Ref: https://leetcode.com/problems/design-circular-deque/solutions/155209/c-99-ring-buffer-no-edge-cases-fb-interviewer-really-loves-it-easy-to-impl-in-4mins-cheers/

#include <vector>

using namespace std;

class MyCircularDeque
{
public:
    vector<int> v;
    int maxSize, front, rear = 0, curSize = 0;
    MyCircularDeque(int k)
    {
        front = k - 1;
        v.resize(k);
        maxSize = k;
    }

    bool insertFront(int value)
    {
        if (isFull())
        {
            return false;
        }
        v[front] = value;
        if (front == 0)
        {
            front = maxSize - 1;
        }
        else
        {
            front -= 1;
        }
        curSize += 1;
        return true;
    }

    bool insertLast(int value)
    {
        if (isFull())
        {
            return false;
        }
        v[rear] = value;
        rear = (rear + 1) % maxSize;
        curSize += 1;
        return true;
    }

    bool deleteFront()
    {
        if (isEmpty())
        {
            return false;
        }
        front = (front + 1) % maxSize;
        curSize -= 1;
        return true;
    }

    bool deleteLast()
    {
        if (isEmpty())
        {
            return false;
        }
        if (rear == 0)
        {
            rear = maxSize - 1;
        }
        else
        {
            rear -= 1;
        }
        curSize -= 1;
        return true;
    }

    int getFront()
    {
        return isEmpty() ? -1 : v[(front + 1) % maxSize];
    }

    int getRear()
    {
        if (isEmpty())
        {
            return -1;
        }
        if (rear == 0)
        {
            return v[maxSize - 1];
        }
        return v[rear - 1];
    }

    bool isEmpty()
    {
        return curSize == 0;
    }

    bool isFull()
    {
        return curSize == maxSize;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */