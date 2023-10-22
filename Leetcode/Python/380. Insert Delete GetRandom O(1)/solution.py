# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.sample(self.set, 1)[0]


class RandomizedSet:    # Ref: https://leetcode.com/problems/insert-delete-getrandom-o1/solutions/85397/simple-solution-in-python/?envType=study-plan-v2&envId=top-interview-150

    def __init__(self):
        self.pos = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.pos:
            # Move last element to deleted element index
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx] = last
            self.pos[last] = idx
            # Delete element
            self.nums.pop()
            self.pos.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
