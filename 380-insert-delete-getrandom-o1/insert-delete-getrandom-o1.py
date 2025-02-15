class RandomizedSet:

    def __init__(self):
        self.data_structure = set()

    def insert(self, val: int) -> bool:
        if val in self.data_structure:
            return False
        self.data_structure.add(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.data_structure:
            self.data_structure.remove(val)
            return True
        
        return False

    def getRandom(self) -> int:
        n=len(self.data_structure)
        k = random.randint(0, n-1)
        count = 0
        for i in self.data_structure:
            if count == k:
                return i
            count += 1
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()