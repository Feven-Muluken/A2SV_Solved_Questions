import random

class RandomizedSet:

    def __init__(self):
        # Just store everything in a list
        self.data = []

    def insert(self, val: int) -> bool:
        # Linear search to check existence
        if val in self.data:
            return False
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Linear search to check existence
        if val not in self.data:
            return False
        self.data.remove(val)  # O(n) operation
        return True

    def getRandom(self) -> int:
        # Pick a random element
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()