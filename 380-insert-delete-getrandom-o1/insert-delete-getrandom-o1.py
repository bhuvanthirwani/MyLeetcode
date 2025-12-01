class RandomizedSet:

    def __init__(self):
        self.map = {}
        self.A=[]

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.A.append(val)
        self.map[val] = len(self.A) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            idx = self.map[val]
            last_val = self.A[len(self.A)-1]
            self.A[idx] = last_val
            self.A.pop()
            self.map[last_val] = idx
            del self.map[val]
            
            return True
        return False

    def getRandom(self) -> int:
        return self.A[random.randint(0, len(self.A)-1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()